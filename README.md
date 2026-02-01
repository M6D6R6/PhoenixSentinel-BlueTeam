**DISCLAIMER – LEGAL NOTICE**  
🔴 **This tool is a proof-of-concept for educational and authorized research purposes only.**  
🔴 It is designed for use in controlled lab environments or with **explicit written permission (RoE)** during authorized penetration testing.  
🔴 **DO NOT** use this tool on any system or network without proper authorization.  
🔴 The author is not responsible for any misuse or damage resulting from the use of this tool.

<p align="center">
  <img src="PhoenixSentinel-BlueTeam.jpg" alt="PhoenixSentinel-BlueTeam Banner" width="500"/>
</p>

# PhoenixSentinel-BlueTeam

Advanced intrusion detection system (IDS) based on artificial intelligence for the Blue Team.

**What it is and what it does**  
PhoenixSentinel-BlueTeam is an AI-powered Intrusion Detection System (IDS) for the Blue Team (defense).  

It analyzes log files (system logs, network traffic, SIEM exports) to:
- Simulate adversarial threats using GAN (to train and test defenses against AI-generated attacks).
- Predict anomalies over time using LSTM (forecasting to anticipate threats).
- Isolate suspicious activity using K-Means clustering + NP-hard graph simulation (to mimic quarantine/containment).

Real-world use: anomaly detection in SOC environments, SIEM data monitoring, proactive network defense.

**For authorized research and Blue Team operations only.**  
**DO NOT** use on unauthorized systems.

**Download & Run – Copy this entire block and paste into your terminal**
```bash
# 1. Download the project
git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git

# 2. Enter the project folder
cd PhoenixSentinel-BlueTeam

# 3. Install all necessary libraries
pip install -r requirements.txt

# 4. Start the program 
python main.py




