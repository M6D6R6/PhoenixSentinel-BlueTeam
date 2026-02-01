<p align="center">
  <img src="PhoenixSentinel-BlueTeam.jpg" alt="PhoenixSentinel-BlueTeam Banner" width="500"/>
</p>
 
 # PhoenixSentinel-BlueTeam

Advanced intrusion detection system (IDS) based on artificial intelligence for the Blue Team.

Features:
- GAN: simulates adversarial threats to train/test defenses
- LSTM: predicts anomalies in time series log data
- K-Means + NP-hard graph: isolates outliers and simulates quarantine

For authorized research and Blue Team operations only.
DO NOT use on unauthorized systems.

## Installation
pip install -r requirements.txt

## Usage and interactive menu
Run the tool:
python main.py

**DISCLAIMER – LEGAL NOTICE**  
This tool is a proof-of-concept for educational and authorized research purposes only.  
It is designed for use in controlled lab environments or with explicit written permission (RoE) during authorized penetration testing.  
DO NOT use this tool on any system or network without proper authorization.  
The author is not responsible for any misuse or damage resulting from the use of this tool.
Upon startup, you will see:
- ASCII header
- Explanation of the tool (actual use in SOC, SIEM, network logs)
- Interactive menu:
1. Analyze a log file (e.g., X_log.txt) show menu and commands
3. Exit open to contributions.

