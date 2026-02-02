import torch
import yaml
import numpy as np
from src.utils.data import load_nsl_kdd
from src.utils.models import GANDiscriminator

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

config = load_config()
device = torch.device('cpu')  # o 'cuda' se hai

# Carica modello Discriminator con input_dim dinamico dal checkpoint
checkpoint = torch.load(config['models']['discriminator'], map_location=device)
input_dim = checkpoint['net.0.weight'].shape[1]  # legge automaticamente dal primo layer
print(f"Input_dim rilevato dal modello salvato: {input_dim}")

disc = GANDiscriminator(input_dim).to(device)
disc.load_state_dict(checkpoint)
disc.eval()

# Carica un piccolo subset per test (usa lo stesso sample_size del training per evitare mismatch feature)
X_test, _, y_test = load_nsl_kdd(
    config['dataset']['train_path'],
    sample_size=config['dataset']['sample_size']  # usa lo stesso del config per coerenza
)

X_tensor = torch.from_numpy(X_test).float().to(device)

# Calcola anomaly scores (score alto = normale, basso = anomalo)
with torch.no_grad():
    scores = disc(X_tensor).cpu().numpy().flatten()

# Statistiche per normali e attacchi
normal_scores = scores[y_test == 0]
attack_scores = scores[y_test == 1]

print(f"\\n=== Risultati anomaly detection (Discriminator score) ===")
print(f"Normali ({len(normal_scores)} campioni):")
print(f"  Mean score: {np.mean(normal_scores):.4f} ± {np.std(normal_scores):.4f}")
print(f"  Min/Max: {np.min(normal_scores):.4f} / {np.max(normal_scores):.4f}")

print(f"\\nAttacchi ({len(attack_scores)} campioni):")
print(f"  Mean score: {np.mean(attack_scores):.4f} ± {np.std(attack_scores):.4f}")
print(f"  Min/Max: {np.min(attack_scores):.4f} / {np.max(attack_scores):.4f}")

# Esempio con threshold (dal config o manuale)
threshold = config['detection']['anomaly_threshold']  # 0.4 dal tuo config
detected_anomalies = np.sum(scores < threshold)
print(f"\\nCon threshold {threshold}:")
print(f"  {detected_anomalies} campioni rilevati come anomali su {len(scores)}")
print(f"  Percentuale rilevata: {detected_anomalies / len(scores) * 100:.1f}%")
print(f"  (Ideale: pochi normali sotto threshold, molti attacchi sotto threshold)")
