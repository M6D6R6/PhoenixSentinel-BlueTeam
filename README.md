
**DISCLAIMER – LEGAL NOTICE**
<span style="color:red; font-weight:bold; border: 2px solid red; padding: 12px; display: block; text-align: center; margin: 10px 0;">
This tool is a proof-of-concept for **educational and authorized research purposes only**.
It is designed for use in controlled lab environments or with **explicit written permission (RoE)** during authorized penetration testing.
**DO NOT** use this tool on any system or network without proper authorization.
The author is not responsible for any misuse or damage resulting from the use of this tool.
</span>

<p align="center">
  <img src="PhoenixSentinel-BlueTeam.jpg" alt="PhoenixSentinel-BlueTeam Banner" width="500"/>
</p>

# PhoenixSentinel-BlueTeam
**AI Blue Team IDS** – GAN threats, **LSTM** forecast, **NetworkX** packet isolation

[![Stars](https://img.shields.io/github/stars/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/stargazers/)
[![Forks](https://img.shields.io/github/forks/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/network/members)
[![MIT License](https://img.shields.io/github/license/M6D6R6/PhoenixSentinel-BlueTeam)](https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/blob/main/LICENSE)

## What it does
**AI-powered IDS** for Blue Team:
- **GAN**: Generate realistic synthetic threats
- **LSTM**: Predict temporal attack patterns
- **NetworkX**: Isolate suspicious packets
- **Scapy**: Live packet analysis

## Step-by-Step Commands
**Step 1: Clone repository**
`git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git`

**Step 2: Enter directory**
`cd PhoenixSentinel-BlueTeam`

**Step 3: Download NSL-KDD dataset**
`kaggle datasets download -d hassan06/nslkdd`

**Step 4: Extract dataset**
`unzip nslkdd.zip -d data/raw_logs/`

**Step 5: Install dependencies**
`pip install torch==2.1.0+cu121 torchvision torchaudio networkx scapy pandas numpy scikit-learn matplotlib seaborn`

**Step 6: Train GAN models (48h GPU)**
`python train_gan.py --epochs 100 --cuda --batch_size 64`

**Step 7: Run live IDS**
`python ids_main.py --live --model-dir models/`

## Live Detection (Scapy)
`sudo PYTHONPATH=$HOME/.local/lib/python3.13/site-packages python3 detect_live.py`

- Generates traffic (ping flood, nmap scan on 192.168.50.101) to test alerts.
- Low score (< 0.4) → anomaly.
- Change threshold in config.yaml for fewer false positives.

**Note**: Live detection richiede sudo per Scapy e interfaccia corretta in config.yaml (es. eth0, wlan0).

**Note**: The tool is operational in a lab environment (training on NSL-KDD, live detection with Scapy).

## License
MIT License – see LICENSE file
