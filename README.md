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

---

## Overview

PhoenixSentinel-BlueTeam is an AI-powered Intrusion Detection System (IDS) **prototype** designed for Blue Team, Red Team simulation, and Digital Forensics lab scenarios.  
The project combines **Generative Adversarial Networks (GAN)**, **LSTM-based time series models**, and **clustering/outlier detection** to analyze logs and (optionally) live network traffic.

**Goal:** Realistic proof-of-concept showing modern AI techniques for threat detection and adversarial simulations in controlled environments.

---

## Features

- **GAN (Generative Adversarial Network)**  
  - Trains on real log data (NSL-KDD features).  
  - Generates synthetic "threat vectors" for advanced/adversarial attacks.  
  - Training via `train_gan.py`, models saved in `models/`.

- **LSTM anomaly forecasting**  
  - Processes log event sequences, outputs anomaly scores.  
  - Detects temporal patterns (scans, bursts, slow attacks).  
  - Training via `train_lstm.py` / `train_Istm.py`.

- **Clustering & outlier isolation**  
  - K-Means clustering + graph-based scoring.  
  - Highlights most suspicious samples for analysts.

- **Interactive AI Blue Team console**  
  - `main.py` provides menu-driven interface.  
  - Train → Test → Live detection in one interface.  
  - Perfect for lab demos and interviews.

- **Live detection (Scapy)**  
  - Real-time packet capture and AI analysis.  
  - **Lab networks + sudo privileges required**.

---

## Repository Structure
