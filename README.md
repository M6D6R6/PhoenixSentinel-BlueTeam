**DISCLAIMER – LEGAL NOTICE**
<span style="color:red; font-weight:bold; border: 2px solid red; padding: 16px; display: block; text-align: center; margin: 20px 0; border-radius: 10px;">
This tool is a **proof-of-concept** developed strictly for **educational, research, and authorized security testing purposes**.<br>
It is intended solely for use in controlled laboratory environments or during penetration testing with **explicit written Rules of Engagement (RoE)** and permission.<br>
**DO NOT** deploy, test or use this tool on any production system, corporate network, or unauthorized infrastructure.<br>
The author assumes **no responsibility** for any misuse, damage, legal consequences or unintended effects resulting from the use of this tool.
</span>

<p align="center">
  <img src="PhoenixSentinel-BlueTeam.jpg" alt="PhoenixSentinel Banner" width="600"/>
</p>

<h1 align="center">PhoenixSentinel – AI-Powered Blue Team Intrusion Detection System</h1>

<p align="center">
  <a href="https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/stargazers"><img src="https://img.shields.io/github/stars/M6D6R6/PhoenixSentinel-BlueTeam?style=social" alt="Stars"></a>
  <a href="https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/network/members"><img src="https://img.shields.io/github/forks/M6D6R6/PhoenixSentinel-BlueTeam?style=social" alt="Forks"></a>
  <a href="https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/blob/main/LICENSE"><img src="https://img.shields.io/github/license/M6D6R6/PhoenixSentinel-BlueTeam" alt="License"></a>
  <a href="https://github.com/M6D6R6/PhoenixSentinel-BlueTeam"><img src="https://img.shields.io/github/repo-size/M6D6R6/PhoenixSentinel-BlueTeam" alt="Repo size"></a>
</p>

PhoenixSentinel is an **AI-driven Intrusion Detection System (IDS) prototype** designed for **Blue Team** operations, **Red Team** simulation, and **Digital Forensics** lab scenarios.

It integrates **Generative Adversarial Networks (GAN)** to generate synthetic threats, **Long Short-Term Memory (LSTM)** for temporal anomaly forecasting, **clustering algorithms** for outlier isolation, and **Scapy** for real-time packet analysis.

The project demonstrates how modern AI techniques can enhance threat detection, adversarial simulation, and proactive defense in controlled environments.

### Core Components & Technologies
- **GAN** – Generates realistic synthetic attack vectors from NSL-KDD features (adversarial training)  
- **LSTM** – Forecasts anomalies in sequential log/traffic data (reconstruction error scoring)  
- **Clustering & Isolation** – K-Means + graph simulation to isolate suspicious samples  
- **Scapy** – Real-time packet sniffing and basic feature extraction  
- **PyTorch** – Deep learning framework for GAN and LSTM  
- **NSL-KDD dataset** – Standard intrusion detection benchmark  

### Current Status & Limitations
Research prototype – **not production-ready**  
High false positives possible in live mode due to basic feature extraction  
Simplified models for educational focus  
CPU-optimized (GPU recommended for GAN training)  
Tested in lab (Kali Linux + Metasploitable 2)  

### Installation & Quick Start

**Clone the repository**
```bash
git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git
cd PhoenixSentinel-BlueTeam
