import os
from termcolor import colored
import subprocess
import sys

def ascii_header():
    art = r"""
      _____  _    _  _____  _____  _   _  _____  _   _  _____ 
     |  __ \| |  | |/ ____|/ ____|| \ | |/ ____|| \ | |/ ____|
     | |__) | |__| | |  __ | |  __ |  \| | |  __ |  \| | (___  
     |  ___/|  __  | | |_ || | |_ || . ` | | |_ || . ` |\___ \ 
     | |    | |  | | |__| || |__| || |\  | |__| || |\  |____) |
     |_|    |_|  |_|\_____|\_____||_| \_|\_____||_| \_|_____/ 
                                                                
      ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗     
      ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     
      ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     
      ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ╚═╝     
      ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗██╗     
      ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     
                                                                
                        AI BLUE TEAM IDS
    """
    print(colored(art, 'cyan', attrs=['bold']))

def print_menu():
    print("\nInteractive Menu:")
    print("1. Train GAN (addestra GAN su NSL-KDD)")
    print("2. Train LSTM (forecasting anomalie)")
    print("3. Test GAN anomaly detection")
    print("4. Test LSTM reconstruction error")
    print("5. Live packet detection (Scapy - richiede sudo)")
    print("6. Exit\n")
    print("Enter command: ", end="")

def main():
    ascii_header()
    print("\n*** AUTHORIZED USE ONLY – For educational/research/authorized pentest/lab only ***")
    print("DO NOT use on unauthorized systems. Author not responsible for misuse.\n")

    while True:
        print_menu()
        choice = input().strip()

        if choice == "1":
            print("\nAvvio training GAN...")
            subprocess.run(["python3", "train_gan.py"])
        elif choice == "2":
            print("\nAvvio training LSTM...")
            subprocess.run(["python3", "train_lstm.py"])
        elif choice == "3":
            print("\nAvvio test GAN anomaly...")
            subprocess.run(["python3", "test_gan_anomaly.py"])
        elif choice == "4":
            print("\nAvvio test LSTM anomaly...")
            subprocess.run(["python3", "test_lstm_anomaly.py"])
        elif choice == "5":
            print("\nAvvio live detection (richiede sudo)...")
            home_path = os.path.expanduser("~")
            python_path = f"{home_path}/.local/lib/python3.13/site-packages"
            subprocess.run(["sudo", "PYTHONPATH=" + python_path, "python3", "detect_live.py"])
        elif choice == "6":
            print("\nExiting PhoenixSentinel. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()