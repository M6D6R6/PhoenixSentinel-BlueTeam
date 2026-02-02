import torch
import torch.nn as nn

class GANGenerator(nn.Module):
    def __init__(self, input_dim, latent_dim=100):
        super(GANGenerator, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(1024, input_dim),
            nn.Tanh()
        )

    def forward(self, z):
        return self.net(z)


class GANDiscriminator(nn.Module):
    def __init__(self, input_dim):
        super(GANDiscriminator, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 1024),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)


class LSTMPredictor(nn.Module):
    def __init__(self, input_dim, hidden_dim=64, num_layers=2):
        super(LSTMPredictor, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers=num_layers, batch_first=True, dropout=0.2)
        self.fc = nn.Linear(hidden_dim, input_dim)  # predice lo stesso numero di feature

    def forward(self, x):
        # x: (batch, seq_len, features)
        out, (h_n, c_n) = self.lstm(x)
        return self.fc(out[:, -1, :])  # prende l'ultimo timestep
