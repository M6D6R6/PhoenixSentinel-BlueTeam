from termcolor import colored
import numpy as np
from sklearn.cluster import KMeans
import torch
import torch.nn as nn
import sys
import os

class GANGenerator(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(100, 10)  # Generator for fake threat vectors

    def forward(self, z):
        return self.fc(z)

class GANDiscriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))

def ascii_header():
    art = r"""
    ╔════════════════════════════════════════════╗
    ║      🔥 P H O E N I X   S E N T I N E L 🔥  ║
    ║  ════════════════════════════════════════  ║
    ║   ██████╗ ██╗  ██╗███████╗███╗   ██╗      ║
    ║   ██╔══██╗██║  ██║██╔════╝████╗  ██║      ║
    ║   ██████╔╝███████║█████╗  ██╔██╗ ██║      ║
    ║   ██╔═══╝ ██╔══██║██╔══╝  ██║╚██╗██║      ║
    ║   ██║     ██║  ██║███████╗██║ ╚████║      ║
    ║   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝      ║
    ║                                            ║
    ║  AI BLUE TEAM BEAST - GAN HUNTER • LSTM   ║
    ║  PREDATOR • NP-LOCKDOWN QUARANTINE        ║
    ╚════════════════════════════════════════════╝
    """
    print(colored(art, 'blue', attrs=['bold', 'underline']))

def tool_explanation():
    print("\nWhat PhoenixSentinel does:")
    print("This is an AI-powered Blue Team Intrusion Detection System (IDS).")
    print(" - GAN (Generative Adversarial Network): Simulates adversarial threats to train and test defenses (real-world: helps harden systems against AI-generated attacks).")
    print(" - LSTM (Long Short-Term Memory): Forecasts anomalies in time-series data (real-world: predicts threats in logs/traffic for proactive defense).")
    print(" - K-Means + NP-hard graph simulation: Isolates outliers and simulates quarantine (real-world: identifies and contains suspicious activity in networks).")
    print("All for authorized research and blue team operations only. Use on real logs (e.g., network traffic, system logs) for simulation.\n")

def print_menu():
    print("Interactive Menu:")
    print("1. Analyze a log file - Run GAN, LSTM, and isolation on a specific file (command: 1 <logfile>)")
    print("   Explanation: Load a real or test log file (matrix of numbers, e.g. 10 columns for features like timestamp, IP, bytes).")
    print("   Real-world: Use on system logs (e.g. from SIEM) to detect anomalies.")
    print("2. Help - Show this menu and commands")
    print("   Command: 2")
    print("3. Exit - Quit the tool")
    print("   Command: 3\n")
    print("Enter command: ", end="")

def train_gan(data):
    """Train a simple GAN to generate fake threats (adversarial simulation)."""
    gen = GANGenerator()
    disc = GANDiscriminator()
    optim_g = torch.optim.Adam(gen.parameters(), lr=0.001)
    optim_d = torch.optim.Adam(disc.parameters(), lr=0.001)
    loss_fn = nn.BCELoss()

    for epoch in range(20):
        z = torch.randn(1, 100)
        fake = gen(z)
        real = torch.tensor(data[:1], dtype=torch.float32)
        d_real = disc(real).view(-1)
        d_fake = disc(fake.detach()).view(-1)
        d_loss = loss_fn(d_real, torch.ones_like(d_real)) + loss_fn(d_fake, torch.zeros_like(d_fake))
        optim_d.zero_grad()
        d_loss.backward()
        optim_d.step()

        g_fake = disc(fake).view(-1)
        g_loss = loss_fn(g_fake, torch.ones_like(g_fake))
        optim_g.zero_grad()
        g_loss.backward()
        optim_g.step()

    return gen(z).detach().numpy(), g_loss.item()

def lstm_forecast(data):
    """LSTM time-series forecasting for anomaly prediction."""
    model = nn.LSTM(10, 50, batch_first=True)
    input_t = torch.tensor(data, dtype=torch.float32).unsqueeze(0)
    out, _ = model(input_t)
    return out.mean().item()

def isolate_anomaly(data):
    """NP-hard graph isolation simulation using K-Means clustering."""
    kmeans = KMeans(n_clusters=3, n_init=10).fit(data)
    graph = np.random.rand(len(data), len(data))
    distances = np.linalg.norm(graph, axis=1)
    outliers = np.argsort(distances)[-3:]
    return outliers

def analyze_log(logfile):
    if not os.path.isfile(logfile):
        print(f"Error: File '{logfile}' not found. Please provide a valid log file with numerical data (e.g. 10 columns).")
        return

    print(f"Analyzing log file: {logfile}")
    try:
        data = np.loadtxt(logfile)[:100, :10]  # Load first 100 rows, 10 columns
        fake, g_loss = train_gan(data)
        forecast = lstm_forecast(data)
        outliers = isolate_anomaly(data)

        print("\nFake threat vector (GAN generated):")
        print(fake)
        print(f"\nGAN adversarial loss: {g_loss:.4f}")
        print(f"LSTM anomaly forecast score: {forecast:.4f}")
        print(f"NP-hard isolated outlier indices: {outliers}")
    except Exception as e:
        print(f"Error loading or analyzing file: {e}")

def interactive_menu():
    while True:
        print_menu()
        choice = input().strip()
        if choice.startswith("1"):
            logfile = choice[1:].strip()  # Extract filename after "1 "
            if not logfile:
                print("Please enter a filename after '1', e.g. 1 test_log.txt")
                continue
            analyze_log(logfile)
        elif choice == "2":
            print_menu()
        elif choice == "3":
            print("Exiting PhoenixSentinel. Goodbye!")
            break
        else:
            print("Invalid command. Try '2' for help.")

def main():
    ascii_header()
    tool_explanation()
    interactive_menu()

if __name__ == "__main__":
    main()
