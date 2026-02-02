**DISCLAIMER – LEGAL NOTICE**
<span style="color:red; font-weight:bold; border: 2px solid red; padding: 12px; display: block; text-align: center; margin: 10px 0;">
This tool is a proof-of-concept for **educational and authorized research purposes only**.<br>
It is designed for use in controlled lab environments or with **explicit written permission (Rules of Engagement)** during authorized penetration testing.<br>
**DO NOT** use this tool on any system, network, or data without proper authorization.<br>
The author is not responsible for any misuse or damage resulting from the use of this tool.
</span>

<p align="center">
  <img src="PhoenixSentinel-BlueTeam.jpg" alt="PhoenixSentinel-BlueTeam Banner" width="500"/>
</p>

# PhoenixSentinel-BlueTeam
**AI Blue Team IDS** – GAN threat generation, LSTM anomaly forecasting, clustering-based isolation, and live packet analysis.

[![Stars](https://img.shields.io/github/stars/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/stargazers/)
[![Forks](https://img.shields.io/github/forks/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/network/members)
[![MIT License](https://img.shields.io/github/license/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/blob/main/LICENSE)

### Overview
PhoenixSentinel-BlueTeam is an **AI-powered Intrusion Detection System (IDS) prototype** designed for Blue Team operations, Red Team simulation, and Digital Forensics lab scenarios.

It combines **Generative Adversarial Networks (GAN)** to simulate synthetic threats, **LSTM** to forecast temporal attack patterns, **clustering** for outlier isolation, and **Scapy** for real-time packet analysis.

**Goal**: Demonstrate how modern AI techniques can enhance threat detection and adversarial simulation in controlled environments.

### Features
- **GAN threat generation**  
  Trains on real log data (NSL-KDD features) to create realistic synthetic attack vectors  
- **LSTM anomaly forecasting**  
  Analyzes log event sequences to predict temporal anomalies  
- **Clustering & isolation**  
  Uses K-Means + graph-based scoring to highlight suspicious samples  
- **Interactive console**  
  `main.py` provides menu-driven interface for training, testing, and live detection  
- **Live packet analysis (Scapy)**  
  Real-time network sniffing with AI-based anomaly scoring  

### Current Status
- Research prototype – **not production-ready**  
- Simplified models for educational focus  
- CPU-optimized (basic GPU support)  
- High false positives possible in live mode due to basic feature extraction  
- Tested in lab environment (Kali + Metasploitable 2)

### Installation

**1. Clone the repository**

git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git
cd PhoenixSentinel-BlueTeam

**2. Setup virtual environment**

python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

**3. Install dependencies**

pip install -r requirements.txt

**4. Download NSL-KDD dataset**

mkdir -p data/raw_logs
kaggle datasets download -d hassan06/nslkdd -p data/raw_logs
cd data/raw_logs && unzip nslkdd.zip && cd ../..

**5. Launch AI Blue Team Console**

python main.py

**6. Live packet analysis (sudo required)**

sudo python3 detect_live.py

**ONE-LINER COMPLETE SETUP**

git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git && cd PhoenixSentinel-BlueTeam && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && mkdir -p data/raw_logs && kaggle datasets download -d hassan06/nslkdd -p data/raw_logs && cd data/raw_logs && unzip nslkdd.zip && cd ../.. && python main.py

**Configuration (config.yaml)**

dataset:
  train_path: data/raw_logs/KDDTrain+.txt
  sample_size: 8000

gan:
  epochs: 50
  device: cpu  # "cuda" for GPU

lstm:
  epochs: 15

detection:
  interface: eth0

**Console Menu**

1. Train GAN (addestra GAN su NSL-KDD)
2. Train LSTM (forecasting anomalie)
3. Test GAN anomaly detection
4. Test LSTM reconstruction error
5. Live packet detection (Scapy - richiede sudo)
6. Exit

**Repository Structure**

├── main.py                 # Interactive console
├── train_gan.py           # GAN training
├── train_lstm.py          # LSTM training
├── detect_live.py         # Live detection
├── config.yaml            # Configuration
├── requirements.txt       # Dependencies
├── data/raw_logs/         # NSL-KDD dataset
├── models/                # Trained models
└── PhoenixSentinel-BlueTeam.jpg

**Limitations & Roadmap**

Current Limitations:

Research prototype only

CPU-focused (GPU support basic)

No production monitoring

Future Improvements:

Docker containerization

ELK Stack integration

Web dashboard + Grafana

Production metrics (ROC curves)
