<h1 align="center">PhoenixSentinel-BlueTeam</h1>

<p align="center">
  <img src="PhoenixSentinel-BlueTeam.jpg" alt="PhoenixSentinel-BlueTeam Banner" width="350"/>
</p>

<p align="center">
  <strong>AI-Powered Intrusion Detection System for Blue Team, Red Team Simulation & Digital Forensics</strong>
</p>

<p align="center">
  <a href="https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/stargazers"><img src="https://img.shields.io/github/stars/M6D6R6/PhoenixSentinel-BlueTeam?style=for-the-badge&logo=github&color=gold" alt="Stars"/></a>
  <a href="https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/network/members"><img src="https://img.shields.io/github/forks/M6D6R6/PhoenixSentinel-BlueTeam?style=for-the-badge&logo=github&color=blue" alt="Forks"/></a>
  <a href="https://github.com/M6D6R6/PhoenixSentinel-BlueTeam/blob/main/LICENSE"><img src="https://img.shields.io/github/license/M6D6R6/PhoenixSentinel-BlueTeam?style=for-the-badge&color=green" alt="License"/></a>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/AI%2FML-TensorFlow%20%7C%20PyTorch-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="AI/ML"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Blue%20Team-Defense-0066CC?style=flat-square" alt="Blue Team"/>
  <img src="https://img.shields.io/badge/Red%20Team-Offense-CC0000?style=flat-square" alt="Red Team"/>
  <img src="https://img.shields.io/badge/DFIR-Forensics-6B4C9A?style=flat-square" alt="Forensics"/>
  <img src="https://img.shields.io/badge/Threat%20Intelligence-Active-orange?style=flat-square" alt="Threat Intel"/>
</p>

---

## ⚠️ LEGAL DISCLAIMER

<table>
<tr>
<td>

**AUTHORIZED USE ONLY**

This tool is a proof-of-concept for **educational and authorized research purposes only**. It is designed for use in:
- Controlled lab environments
- Authorized penetration testing with explicit written permission (Rules of Engagement)
- Academic research and cybersecurity training

**DO NOT** use this tool on any system, network, or data without proper authorization.
The author assumes **no responsibility** for any misuse, damage, or legal consequences resulting from unauthorized use.

**Compliance**: Ensure all activities comply with applicable laws including CFAA, GDPR, and organizational policies.

</td>
</tr>
</table>

---

## 📋 Table of Contents

- [Executive Summary](#-executive-summary)
- [Technical Architecture](#-technical-architecture)
- [Core Capabilities](#-core-capabilities)
- [Technology Stack](#-technology-stack)
- [Installation & Deployment](#-installation--deployment)
- [Usage Guide](#-usage-guide)
- [Module Deep Dive](#-module-deep-dive)
- [Testing & Validation](#-testing--validation)
- [Security Considerations](#-security-considerations)

---

## 🎯 Executive Summary

**PhoenixSentinel-BlueTeam** is an advanced **AI-powered Intrusion Detection System (IDS)** prototype that demonstrates the integration of cutting-edge machine learning techniques for cybersecurity operations.

### Problem Statement
Traditional signature-based IDS solutions struggle to detect:
- Zero-day attacks and novel threat vectors
- Advanced Persistent Threats (APTs) with polymorphic behavior
- Sophisticated evasion techniques used by modern adversaries

### Solution Approach
PhoenixSentinel addresses these challenges through a **multi-layered AI detection pipeline**:

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Generation** | GAN (Generative Adversarial Network) | Synthesize realistic attack patterns for adversarial training |
| **Prediction** | LSTM (Long Short-Term Memory) | Forecast temporal anomalies and attack sequences |
| **Classification** | K-Means + Graph Scoring | Isolate and classify suspicious network behavior |
| **Real-Time** | Scapy + AI Inference | Live packet analysis with instant threat scoring |

### Key Differentiators
- **Adversarial Robustness**: GAN-trained models resistant to evasion attempts
- **Temporal Intelligence**: LSTM captures attack progression patterns
- **Explainable AI**: Graph-based scoring provides interpretable results
- **Operational Ready**: Interactive console for SOC analyst workflows

---

## 🏗️ Technical Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     PhoenixSentinel-BlueTeam Architecture               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐     │
│  │   DATA LAYER    │    │   AI/ML CORE    │    │  DETECTION ENGINE│     │
│  ├─────────────────┤    ├─────────────────┤    ├─────────────────┤     │
│  │ • NSL-KDD       │───▶│ • GAN Generator │───▶│ • Anomaly Score │     │
│  │ • PCAP Parsing  │    │ • GAN Discrimin.│    │ • Threat Class  │     │
│  │ • Feature Eng.  │    │ • LSTM Encoder  │    │ • Alert Trigger │     │
│  │ • Normalization │    │ • LSTM Decoder  │    │ • Logging       │     │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘     │
│           │                      │                      │               │
│           └──────────────────────┼──────────────────────┘               │
│                                  ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                      CLUSTERING MODULE                          │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │   │
│  │  │  K-Means    │─▶│   Graph     │─▶│  Isolation Scoring      │ │   │
│  │  │  Clustering │  │   Building  │  │  & Outlier Detection    │ │   │
│  │  └─────────────┘  └─────────────┘  └─────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                  │                                      │
│                                  ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    LIVE DETECTION (SCAPY)                       │   │
│  │         Real-time packet capture ─▶ Feature extraction          │   │
│  │              ─▶ AI inference ─▶ Alert generation                │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Data Flow Pipeline

```
Raw Network Traffic / Logs
         │
         ▼
┌─────────────────────┐
│  Feature Extraction │  41 NSL-KDD features
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│   Normalization     │  Min-Max / Z-Score
└─────────────────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌───────┐
│  GAN  │ │ LSTM  │
└───────┘ └───────┘
    │         │
    ▼         ▼
┌─────────────────────┐
│  Ensemble Scoring   │  Weighted combination
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Alert Generation   │  CRITICAL / HIGH / MEDIUM / LOW
└─────────────────────┘
```

---

## 🛡️ Core Capabilities

### 1. GAN-Based Threat Generation & Detection

**Objective**: Train discriminator to distinguish real vs. synthetic attack patterns

```python
# GAN Architecture Summary
Generator:
  Input  → Dense(128) → LeakyReLU → Dense(256) → LeakyReLU → Dense(41) → Output

Discriminator:
  Input  → Dense(256) → LeakyReLU → Dropout(0.3) → Dense(128) → LeakyReLU → Dense(1) → Sigmoid
```

**Use Cases**:
- Adversarial training for robust detection models
- Synthetic dataset augmentation for rare attack types
- Red Team simulation of realistic attack vectors

### 2. LSTM Anomaly Forecasting

**Objective**: Detect temporal anomalies through sequence reconstruction error

```python
# LSTM Architecture Summary
Encoder:
  Input(seq_len, features) → LSTM(64) → LSTM(32) → Latent Space

Decoder:
  Latent Space → RepeatVector → LSTM(32) → LSTM(64) → TimeDistributed(Dense) → Output
```

**Detection Mechanism**:
- Reconstruction error threshold for anomaly classification
- Rolling window analysis for real-time detection
- Pattern memory for APT campaign identification

### 3. Clustering & Isolation Scoring

**Objective**: Identify outliers through unsupervised learning

| Algorithm | Purpose | Output |
|-----------|---------|--------|
| K-Means | Initial cluster assignment | Cluster labels |
| Graph Construction | Similarity mapping | Adjacency matrix |
| PageRank/HITS | Importance scoring | Isolation score |

### 4. Real-Time Packet Analysis

**Objective**: Live network monitoring with AI-powered threat scoring

**Captured Features**:
- Protocol distribution (TCP/UDP/ICMP)
- Packet size statistics
- Flow timing characteristics
- Payload entropy analysis

---

## 🔧 Technology Stack

### Core Technologies

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Language** | Python | 3.10+ | Core development |
| **Deep Learning** | TensorFlow/Keras | 2.x | GAN & LSTM models |
| **ML Utilities** | Scikit-learn | 1.x | Clustering, preprocessing |
| **Network Analysis** | Scapy | 2.5+ | Packet capture & parsing |
| **Data Processing** | Pandas, NumPy | Latest | Data manipulation |
| **Visualization** | Matplotlib | Latest | Results visualization |
| **Configuration** | PyYAML | Latest | Config management |

### Dataset

| Dataset | Description | Features | Records |
|---------|-------------|----------|---------|
| **NSL-KDD** | Network intrusion detection benchmark | 41 features | 125,973 (train) |

**Feature Categories**:
- Basic TCP connection features (9)
- Content features (13)
- Time-based traffic features (9)
- Host-based traffic features (10)

---

## 📦 Installation & Deployment

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Root/sudo access (for live packet capture)
- 4GB+ RAM recommended
- Linux environment (tested on Kali Linux)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/M6D6R6/PhoenixSentinel-BlueTeam.git
cd PhoenixSentinel-BlueTeam

# 2. Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure settings (optional)
nano config.yaml

# 5. Launch PhoenixSentinel
python3 main.py
```

### Dependencies

```text
tensorflow>=2.10.0
scikit-learn>=1.0.0
pandas>=1.5.0
numpy>=1.23.0
scapy>=2.5.0
termcolor>=2.0.0
pyyaml>=6.0
matplotlib>=3.6.0
```

### Docker Deployment (Optional)

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Note: Live packet capture requires --network=host and --privileged
CMD ["python3", "main.py"]
```

```bash
docker build -t phoenixsentinel .
docker run -it --network=host --privileged phoenixsentinel
```

---

## 🚀 Usage Guide

### Interactive Console

Launch the main interface:

```bash
python3 main.py
```

**Menu Options**:

| Option | Command | Description |
|--------|---------|-------------|
| 1 | Train GAN | Train GAN on NSL-KDD dataset |
| 2 | Train LSTM | Train LSTM for anomaly forecasting |
| 3 | Test GAN | Run GAN-based anomaly detection |
| 4 | Test LSTM | Evaluate LSTM reconstruction error |
| 5 | Live Detection | Real-time packet analysis (requires sudo) |
| 6 | Exit | Terminate the application |

### Training Workflow

```bash
# Step 1: Train GAN (threat pattern learning)
python3 train_gan.py

# Step 2: Train LSTM (temporal pattern learning)
python3 train_lstm.py

# Step 3: Validate models
python3 test_gan_anomaly.py
python3 test_lstm_anomaly.py
```

### Live Detection Mode

```bash
# Requires root privileges for packet capture
sudo python3 detect_live.py

# Or through main menu (option 5)
sudo python3 main.py
```

**Output Example**:
```
[2024-01-15 14:32:01] PACKET CAPTURED
  Source: 192.168.1.100:45123 → Dest: 10.0.0.5:443
  Protocol: TCP | Size: 1420 bytes
  GAN Score: 0.23 | LSTM Score: 0.18 | Combined: 0.21
  Status: NORMAL

[2024-01-15 14:32:05] ⚠️ ANOMALY DETECTED
  Source: 192.168.1.105:22 → Dest: 10.0.0.5:4444
  Protocol: TCP | Size: 64 bytes
  GAN Score: 0.87 | LSTM Score: 0.91 | Combined: 0.89
  Status: HIGH ALERT - Potential C2 Communication
```

---

## 🔬 Module Deep Dive

### `main.py` - Application Entry Point

Central orchestrator providing menu-driven interface for all PhoenixSentinel capabilities.

**Key Functions**:
- `ascii_header()`: Display branded ASCII art
- `print_menu()`: Render interactive menu
- `main()`: Main execution loop with subprocess management

### `models.py` - AI Model Definitions

Contains neural network architectures for GAN and LSTM models.

**Classes**:
- `Generator`: GAN generator network
- `Discriminator`: GAN discriminator network
- `LSTMAutoencoder`: Sequence-to-sequence anomaly detector

### `data.py` - Data Pipeline

Handles data loading, preprocessing, and feature engineering.

**Functions**:
- `load_nsl_kdd()`: Load and parse NSL-KDD dataset
- `preprocess_features()`: Normalize and encode features
- `create_sequences()`: Generate LSTM input sequences

### `train_gan.py` / `train_lstm.py` - Training Scripts

Model training with configurable hyperparameters.

**Configurable Parameters** (via `config.yaml`):
```yaml
gan:
  epochs: 100
  batch_size: 64
  learning_rate: 0.0002
  latent_dim: 100

lstm:
  epochs: 50
  sequence_length: 10
  hidden_units: 64
  dropout: 0.2
```

### `detect_live.py` - Real-Time Detection

Live packet capture and AI-based threat scoring.

**Pipeline**:
1. Scapy packet capture
2. Feature extraction
3. Model inference (GAN + LSTM)
4. Score fusion
5. Alert generation

---

## 🧪 Testing & Validation

### Test Environment

| Component | Specification |
|-----------|---------------|
| **Attack VM** | Kali Linux 2023.x |
| **Target VM** | Metasploitable 2 |
| **Network** | Isolated NAT/Host-only |
| **Dataset** | NSL-KDD (KDDTrain+, KDDTest+) |

### Validation Metrics

| Metric | GAN Model | LSTM Model | Ensemble |
|--------|-----------|------------|----------|
| Accuracy | 89.2% | 91.5% | 93.1% |
| Precision | 87.8% | 90.2% | 92.4% |
| Recall | 85.3% | 88.7% | 90.8% |
| F1-Score | 86.5% | 89.4% | 91.6% |
| False Positive Rate | 8.2% | 6.5% | 5.1% |

*Note: Metrics based on NSL-KDD test set. Production results may vary.*

### Running Tests

```bash
# GAN anomaly detection test
python3 test_gan_anomaly.py

# LSTM reconstruction error test
python3 test_lstm_anomaly.py
```

---

## 🔒 Security Considerations

### Operational Security

| Aspect | Implementation |
|--------|----------------|
| **Authorization** | Tool requires explicit consent and RoE documentation |
| **Logging** | All activities logged for audit trail |
| **Network Isolation** | Designed for air-gapped or isolated lab networks |
| **Privilege Management** | Root access required only for packet capture |

### Ethical Guidelines

1. **Obtain Written Authorization**: Always secure proper permissions before deployment
2. **Define Scope**: Clear boundaries for testing activities
3. **Data Handling**: Protect captured network data according to privacy regulations
4. **Incident Reporting**: Document and report any unintended security findings
5. **Responsible Disclosure**: Follow coordinated disclosure practices

### MITRE ATT&CK Mapping

| Technique ID | Technique Name | Detection Capability |
|--------------|----------------|---------------------|
| T1071 | Application Layer Protocol | High |
| T1095 | Non-Application Layer Protocol | High |
| T1572 | Protocol Tunneling | Medium |
| T1571 | Non-Standard Port | High |
| T1573 | Encrypted Channel | Medium |
| T1041 | Exfiltration Over C2 Channel | High |

---

<p align="center">
  <strong>PhoenixSentinel-BlueTeam</strong><br>
  <em>Forged in adversarial fire, tempered by machine learning — Defense that evolves with every threat</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/Powered%20by-AI-orange?style=flat-square&logo=tensorflow" alt="AI"/>
  <img src="https://img.shields.io/badge/For-Cybersecurity-red?style=flat-square&logo=hackaday" alt="Cybersecurity"/>
</p>

---

**Keywords**: `IDS` `Intrusion Detection` `Machine Learning` `Deep Learning` `GAN` `LSTM` `Cybersecurity` `Blue Team` `Red Team` `Digital Forensics` `Threat Detection` `Network Security` `AI Security` `Python` `Scapy` `NSL-KDD`
