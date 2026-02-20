import os
import subprocess

print("=== USER INFOS ===")
os.system("whoami")
os.system("id")

print("\n=== KERNEL INFO ===")
os.system("uname -a")

print("\n=== OPEN PORTS ===")
os.system("ss -tuln")

print("\n=== RUNNING PROCESSES")
os.system("ps aux | head -n 10")