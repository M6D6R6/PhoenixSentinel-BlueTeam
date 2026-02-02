import torch
import yaml
import numpy as np
import pickle
import pandas as pd
from src.utils.models import LSTMPredictor

# Colonne NSL-KDD (copia da data.py per sicurezza)
NSL_COLUMNS = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
    'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
    'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count',
    'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
    'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate', 'label', 'difficulty'
]

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

config = load_config()
device = torch.device('cpu')

# Carica modello LSTM
checkpoint = torch.load(config['models']['lstm'], map_location=device)
input_dim = checkpoint['lstm.weight_ih_l0'].shape[1]
print(f"Input_dim dal modello: {input_dim}")

model = LSTMPredictor(input_dim, config['lstm']['hidden_dim']).to(device)
model.load_state_dict(checkpoint)
model.eval()

# Carica preprocessor salvato
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

# Carica raw data test (2000 righe, stesso random seed)
df_test = pd.read_csv(config['dataset']['train_path'], names=NSL_COLUMNS, header=None)
df_test = df_test.sample(n=2000, random_state=42)
y_test = (df_test['label'] != 'normal').astype(int)
X_raw = df_test.drop(['label', 'difficulty'], axis=1)

# Trasforma con preprocessor salvato
X_test = preprocessor.transform(X_raw)
print(f"Test set shape: {X_test.shape}")

X_tensor = torch.from_numpy(X_test).unsqueeze(1).float().to(device)

with torch.no_grad():
    pred = model(X_tensor)
    errors = np.mean((pred.cpu().numpy() - X_test)**2, axis=1)

normal_errors = errors[y_test == 0]
attack_errors = errors[y_test == 1]

print(f"\\n=== LSTM Reconstruction Error (MSE) ===")
print(f"Normali ({len(normal_errors)} campioni):")
print(f"  Mean error: {np.mean(normal_errors):.6f} ± {np.std(normal_errors):.6f}")
print(f"  Min/Max: {np.min(normal_errors):.6f} / {np.max(normal_errors):.6f}")

print(f"\\nAttacchi ({len(attack_errors)} campioni):")
print(f"  Mean error: {np.mean(attack_errors):.6f} ± {np.std(attack_errors):.6f}")
print(f"  Min/Max: {np.min(attack_errors):.6f} / {np.max(attack_errors):.6f}")

threshold = np.mean(normal_errors) + 3 * np.std(normal_errors)
detected = np.sum(errors > threshold)
print(f"\\nThreshold {threshold:.6f} (mean normal + 3*std):")
print(f"  {detected} anomalie rilevate su {len(errors)} ({detected/len(errors)*100:.1f}%)")
print("  (Ideale: errori attacchi molto più alti dei normali)")
