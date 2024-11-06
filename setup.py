import os
import subprocess
from setuptools import setup
from setuptools.command.install import install

# Colors for console output
GREEN = "\033[1;32m"
RESET = "\033[0m"
BLUE  = "\033[1;34m"


print(f"\n{BLUE}[+] Sparta installation...{RESET}")
SPARTA_DIR = os.getcwd()
VENV_DIR = os.path.join(SPARTA_DIR, "spartaEnv")
VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python")
REQUIREMENTS_PATH = os.path.join(SPARTA_DIR, "requirements.txt")


# Step 1: Remove old virtual environment
print(f"{BLUE}[+] Removing any previous virtual environment{RESET}")
subprocess.run(["rm", "-rf", VENV_DIR], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Step 2: Create virtual environment
subprocess.run(["/usr/bin/env", "python3", "-m", "venv", VENV_DIR], check=True)
print(f"{BLUE}[+] Sparta virtual environment created{RESET}")

# Step 3: Install requirements with quiet mode
subprocess.run([VENV_PYTHON, "-m", "pip", "install", "-r", REQUIREMENTS_PATH, "-q"], check=True)
print(f"{BLUE}[+] Pip requirements installed within venv{RESET}")

# Step 14: make sparta available system-wide
subprocess.run(['sudo', 'bash', '-c', "echo '#!/bin/bash' > /usr/bin/sparta"], check=True)
subprocess.run(['sudo', 'bash', '-c', f"echo 'cd {SPARTA_DIR} && nohup /usr/bin/env python3 sparta.py > sparta.log 2>&1 &' >> /usr/bin/sparta"], check=True)
subprocess.run(['sudo', 'bash', '-c', "chmod +x /usr/bin/sparta"], check=True)
print(f"{GREEN}[!] Sparta tool now available system-wide by typing : sparta{RESET}")

# Final instruction message
print(f"{BLUE}[+] Installation complete!{RESET}")
print(f"{BLUE}[+] Instructions :{RESET}")
print(f"1. {GREEN}Navigate to the Sparta directory:{RESET} cd {SPARTA_DIR}")
print(f"2. {GREEN}Activate the virtual environment:{RESET} source spartaEnv/bin/activate")
print(f"3. {GREEN}Run the Sparta script directly from the directory:{RESET} python3 sparta.py")
print(f"   {GREEN}OR{RESET}")
print(f"   {GREEN}Run sparta system-wide use :{RESET} sparta")
print(f"4. {GREEN}When done, deactivate the virtual environment:{RESET} deactivate\n")
