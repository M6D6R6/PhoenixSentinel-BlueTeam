import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import yaml
from src.utils.data import load_nsl_kdd
from src.utils.models import GANGenerator, GANDiscriminator

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

def train():
    config = load_config()
    device = torch.device('cuda' if config['gan']['device'] == 'cuda' and torch.cuda.is_available() else 'cpu')
    print(f"Usando device: {device}")

    # Carica dataset (solo features, ignora label per GAN unsupervised)
    X, _, _ = load_nsl_kdd(
        config['dataset']['train_path'],
        sample_size=config['dataset']['sample_size']
    )
    print(f"Dataset caricato: {X.shape}")

    input_dim = X.shape[1]
    latent_dim = config['gan']['latent_dim']

    generator = GANGenerator(input_dim, latent_dim).to(device)
    discriminator = GANDiscriminator(input_dim).to(device)

    optim_g = optim.Adam(generator.parameters(), lr=config['gan']['lr'], betas=(0.5, 0.999))
    optim_d = optim.Adam(discriminator.parameters(), lr=config['gan']['lr'], betas=(0.5, 0.999))

    criterion = nn.BCELoss()

    dataset = TensorDataset(torch.from_numpy(X))
    loader = DataLoader(dataset, batch_size=config['gan']['batch_size'], shuffle=True)

    epochs = config['gan']['epochs']
    for epoch in range(epochs):
        d_losses = []
        g_losses = []

        for real_batch in loader:
            real = real_batch[0].to(device)
            batch_size = real.size(0)

            # Train Discriminator
            optim_d.zero_grad()
            z = torch.randn(batch_size, latent_dim).to(device)
            fake = generator(z).detach()
            d_real = discriminator(real).view(-1)
            d_fake = discriminator(fake).view(-1)
            d_loss = criterion(d_real, torch.ones_like(d_real)) + criterion(d_fake, torch.zeros_like(d_fake))
            d_loss.backward()
            optim_d.step()
            d_losses.append(d_loss.item())

            # Train Generator
            optim_g.zero_grad()
            fake = generator(z)
            g_fake = discriminator(fake).view(-1)
            g_loss = criterion(g_fake, torch.ones_like(g_fake))
            g_loss.backward()
            optim_g.step()
            g_losses.append(g_loss.item())

        avg_d_loss = np.mean(d_losses)
        avg_g_loss = np.mean(g_losses)
        print(f"Epoch [{epoch+1}/{epochs}] | D_loss: {avg_d_loss:.4f} | G_loss: {avg_g_loss:.4f}")

    # Salva modelli
    torch.save(generator.state_dict(), config['models']['generator'])
    torch.save(discriminator.state_dict(), config['models']['discriminator'])
    print("Training GAN completato! Modelli salvati.")

if __name__ == "__main__":
    train()
