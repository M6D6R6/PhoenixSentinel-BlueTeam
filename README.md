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

Upon startup, you will see:
- ASCII header
- Explanation of the tool (actual use in SOC, SIEM, network logs)
- Interactive menu:
1. Analyze a log file (e.g., X_log.txt) show menu and commands
3. Exit open to contributions.

