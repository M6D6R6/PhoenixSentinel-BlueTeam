**DISCLAIMER – LEGAL NOTICE**
<span style="color:red; font-weight:bold; border: 2px solid red; padding: 12px; display: block; text-align: center; margin: 10px 0;">
This tool is a proof-of-concept for <b>educational and authorized research purposes only</b>.<br>
It is designed for use in controlled lab environments or with <b>explicit written permission (Rules of Engagement)</b> during authorized penetration testing.<br>
<b>DO NOT</b> use this tool on any system, network, or data without proper authorization.<br>
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
PhoenixSentinel-BlueTeam is an AI-powered Intrusion Detection System (IDS) prototype designed for Blue Team operations, Red Team simulation, and Digital Forensics lab scenarios. It combines Generative Adversarial Networks (GAN) to simulate synthetic threats, LSTM to forecast temporal attack patterns, clustering for outlier isolation, and Scapy for real-time packet analysis. The goal is to demonstrate how modern AI techniques can enhance threat detection and adversarial simulation in controlled environments. Current status: research prototype – not production-ready. Simplified models for educational focus. CPU-optimized (basic GPU support). High false positives possible in live mode due to basic feature extraction. Tested in lab environment (Kali + Metasploitable 2). Installation and quick start: git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git
cd PhoenixSentinel-BlueTeam
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
kaggle datasets download -d hassan06/nslkdd
unzip nslkdd.zip -d data/raw_logs/
rm nslkdd.zip
python3 main.py
sudo PYTHONPATH=$HOME/.local/lib/python3.13/site-packages python3 detect_live.py
Menu options in main.py: 1 → Train GAN, 2 → Train LSTM, 3 → Test GAN anomaly detection, 4 → Test LSTM reconstruction error, 5 → Live packet detection (requires sudo), 6 → Exit. Live packet detection requires root privileges and correct interface in config.yaml (e.g. eth0, wlan0 – check with ip link). Generate test traffic (e.g. nmap -A 192.168.50.101, ping flood) to trigger alerts. Low score (< threshold) → anomaly detected. Technical notes: Training GAN may take 24–48 hours on GPU for optimal results (current config uses reduced epochs for demo). Live mode uses basic feature extraction (packet length, TTL, protocol). Real-world use requires richer features (flow stats, payload analysis). Threshold: default 0.4 – adjust in config.yaml to balance false positives/negatives. Hardware: tested on CPU (Kali Linux). GPU strongly recommended for GAN training. Future improvements: advanced GAN variants (WGAN-GP, CycleGAN), flow-based features (Zeek/Argus integration), real-time visualization dashboard, autoencoder + LSTM hybrid, adversarial robustness testing, containerization (Docker). License: MIT License – see LICENSE file. Developed for educational and authorized research purposes only.
