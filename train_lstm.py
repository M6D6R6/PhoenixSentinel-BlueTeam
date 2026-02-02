import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import yaml
import pickle  # import in cima
from src.utils.data import load_nsl_kdd
from src.utils.models import LSTMPredictor

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

def train():
    config = load_config()
    device = torch.device('cpu')

    # Carica dati e preprocessor
    X, preprocessor, _ = load_nsl_kdd(
        config['dataset']['train_path'],
        sample_size=config['dataset']['sample_size']
    )
    print(f"Dataset caricato: {X.shape}")

    # Salva preprocessor per test futuri
    with open('preprocessor.pkl', 'wb') as f:
        pickle.dump(preprocessor, f)

    input_dim = X.shape[1]
    model = LSTMPredictor(input_dim, config['lstm']['hidden_dim']).to(device)

    optimizer = optim.Adam(model.parameters(), lr=config['lstm']['lr'])
    criterion = nn.MSELoss()

    # Shift for forecasting (time-series style)
    X_input = torch.from_numpy(X[:-1]).unsqueeze(1).float().to(device)
    y_target = torch.from_numpy(X[1:]).float().to(device)

    dataset = TensorDataset(X_input, y_target)
    loader = DataLoader(dataset, batch_size=config['lstm']['batch_size'], shuffle=False)

    epochs = config['lstm']['epochs']
    for epoch in range(epochs):
        losses = []
        for inputs, targets in loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            losses.append(loss.item())
        avg_loss = np.mean(losses)
        print(f"Epoch [{epoch+1}/{epochs}] | Loss: {avg_loss:.4f}")

    torch.save(model.state_dict(), config['models']['lstm'])
    print("Training LSTM completato! Preprocessor salvato in preprocessor.pkl")

if __name__ == "__main__":
    train()
