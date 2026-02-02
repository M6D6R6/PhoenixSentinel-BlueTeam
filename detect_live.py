from scapy.all import sniff, IP
import torch
import yaml
import numpy as np
from src.utils.models import GANDiscriminator

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

config = load_config()
device = torch.device('cpu')

# Carica Discriminator (usa GAN per anomaly score)
checkpoint = torch.load(config['models']['discriminator'], map_location=device)
input_dim = checkpoint['net.0.weight'].shape[1]

disc = GANDiscriminator(input_dim).to(device)
disc.load_state_dict(checkpoint)
disc.eval()

def extract_features(pkt):
    features = np.zeros(input_dim)
    if IP in pkt:
        features[0] = pkt[IP].len or 0
        features[1] = pkt[IP].ttl or 0
        # Aggiungi altri se vuoi (per ora semplice)
    return features

def process_packet(pkt):
    features = extract_features(pkt)
    input_t = torch.from_numpy(features).float().unsqueeze(0).to(device)
    score = disc(input_t).item()
    if score < config['detection']['anomaly_threshold']:
        print(f"[ALERT] Anomalo: {pkt.summary()} | Score: {score:.4f}")

print("Sniffing live su interface:", config['detection']['interface'])
print("Ctrl+C per fermare")
sniff(iface=config['detection']['interface'], prn=process_packet, store=0)
