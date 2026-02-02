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

## Overview
PhoenixSentinel-BlueTeam is an **AI-powered Intrusion Detection System (IDS) prototype** designed for Blue Team operations, Red Team simulation, and Digital Forensics lab scenarios.

**Core AI Technologies:**
- **GAN** - Synthetic threat generation
- **LSTM** - Temporal anomaly forecasting  
- **K-Means** - Outlier isolation
- **Scapy** - Real-time packet analysis

## 🚀 Installation 

### **Complete Setup**

``bash
# 1. Clone repository
git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git
cd PhoenixSentinel-BlueTeam

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download dataset (Kaggle account required)
mkdir -p data/raw_logs
kaggle datasets download -d hassan06/nslkdd -p data/raw_logs
cd data/raw_logs && unzip nslkdd.zip && cd ../..

# 5. Launch console
python main.py

# 6. Live analysis (sudo required)
sudo python3 detect_live.py

### **ONE-LINER**

