from datetime import datetime
import subprocess
import os

def check_aws():
    return subprocess.run(["chcp", "65001", "&&", "ping", "63.176.0.0"], text=True, capture_output=True, shell=True).stdout.strip() + "\n\n"

def check_discord():
    return subprocess.run(["chcp", "65001", "&&", "ping", "discord.com"], text=True, capture_output=True, shell=True).stdout.strip() + "\n\n"

def check_youtube():
    return subprocess.run(["chcp", "65001", "&&", "ping", "youtube.com"], text=True, capture_output=True, shell=True).stdout.strip() + "\n\n"

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("log.txt", "w", encoding="utf-8") as file:
    file.write(check_aws())
    file.write(check_discord())
    file.write(check_youtube())

subprocess.run(["git", "add", "."], text=True, capture_output=True)
subprocess.run(["git", "commit", "-m", f"Checking at {datetime.now().astimezone().isoformat(timespec="minutes")}"], text=True, capture_output=True)
subprocess.run(["git", "push", "-u", "origin", "main"], text=True, capture_output=True)

