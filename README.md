**DISCLAIMER – LEGAL NOTICE**
<span style="color:red; font-weight:bold; border: 2px solid red; padding: 12px; display: block; text-align: center; margin: 10px 0;">
This tool is a proof-of-concept for <b>educational and authorized research purposes only</b>.

It is designed for use in controlled lab environments or with <b>explicit written permission (Rules of Engagement)</b> during authorized penetration testing.

<b>DO NOT</b> use this tool on any system, network, or data without proper authorization.

The author is not responsible for any misuse or damage resulting from the use of this tool.
</span>
<p align="center">
&nbsp;&nbsp;<img src="PhoenixSentinel-BlueTeam.jpg" alt="PhoenixSentinel-BlueTeam Banner" width="500"/>
</p>
# PhoenixSentinel-BlueTeam
**AI Blue Team IDS** – GAN threat generation, LSTM anomaly forecasting, clustering-based isolation, and live packet analysis.
[![Stars](https://img.shields.io/github/stars/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/stargazers/)
[![Forks](https://img.shields.io/github/forks/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/network/members)
[![MIT License](https://img.shields.io/github/license/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/blob/main/LICENSE)
---
## Overview
PhoenixSentinel-BlueTeam is an AI-powered Intrusion Detection System (IDS) **prototype** designed for Blue Team, Red Team simulation, and Digital Forensics lab scenarios.
The project combines **Generative Adversarial Networks (GAN)**, **LSTM-based time series models**, and **clustering/outlier detection** to analyze logs and (optionally) live network traffic.
**Goal:** Realistic proof-of-concept showing modern AI techniques for threat detection and adversarial simulations in controlled environments.
---
## Features
- **GAN (Generative Adversarial Network)**
&nbsp;&nbsp;- Trains on real log data (NSL-KDD features).
&nbsp;&nbsp;- Generates synthetic "threat vectors" for advanced/adversarial attacks.
&nbsp;&nbsp;- Training via `train_gan.py`, models saved in `models/`.
- **LSTM anomaly forecasting**
&nbsp;&nbsp;- Processes log event sequences, outputs anomaly scores.
&nbsp;&nbsp;- Detects temporal patterns (scans, bursts, slow attacks).
&nbsp;&nbsp;- Training via `train_lstm.py` / `train_Istm.py`.
- **Clustering & outlier isolation**
&nbsp;&nbsp;- K-Means clustering + graph-based scoring.
&nbsp;&nbsp;- Highlights most suspicious samples for analysts.
- **Interactive AI Blue Team console**
&nbsp;&nbsp;- `main.py` provides menu-driven interface.
&nbsp;&nbsp;- Train → Test → Live detection in one interface.
&nbsp;&nbsp;- Perfect for lab demos and interviews.
- **Live detection (Scapy)**
&nbsp;&nbsp;- Real-time packet capture and AI analysis.
&nbsp;&nbsp;- **Lab networks + sudo privileges required**.
---
## Repository Structure
---
## Installation
**Recommended: Python virtual environment**
```bash
# 1. Clone the repository
git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git
cd PhoenixSentinel-BlueTeam
# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
# 3. Install dependencies
pip install -r requirements.txt
# Create data directory
mkdir -p data/raw_logs
# Download NSL-KDD (Kaggle CLI - requires kaggle account)
kaggle datasets download -d hassan06/nslkdd -p data/raw_logs
cd data/raw_logs && unzip nslkdd.zip && cd ../..
dataset:
  train_path: data/raw_logs/KDDTrain+.txt
  sample_size: 8000 # Small sample for quick testing
gan:
  latent_dim: 100
  epochs: 50
  batch_size: 64
  lr: 0.0001
  device: cpu # Change to "cuda" for GPU
lstm:
  hidden_dim: 64
  epochs: 15
  batch_size: 64
  lr: 0.001
detection:
  anomaly_threshold: 0.4
  interface: eth0 # Change to your network interface
models:
  generator: models/gan_generator.pth
  discriminator: models/gan_discriminator.pth
  lstm: models/lstm_predictor.pth
python main.py
sudo python3 detect_live.py
Limitations & Roadmap
Current Limitations
• Research prototype - not production-ready
• Simplified GAN/LSTM architectures for educational focus
• CPU-optimized (basic GPU support)
• No automated testing or production monitoring
Planned Improvements
• Web dashboard with real-time alerts and visualizations
• Integration with ELK Stack, Splunk
• Production metrics (ROC curves, precision-recall)
• Advanced feature engineering from SIEM logs
• Containerization (Docker)
```
