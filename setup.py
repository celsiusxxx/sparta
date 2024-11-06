import os
import subprocess
from setuptools import setup
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        # Colors for console output
        GREEN = "\033[1;32m"
        RESET = "\033[0m"
        BLUE  = "\033[1;34m"

        # Define the installation steps
        SPARTA_DIR = os.path.join("/home/kali/tools/sparta")
        VENV_DIR = os.path.join(SPARTA_DIR, "spartaEnv")

        # Step 1: Create virtual environment
        subprocess.run(["/usr/bin/env", "python", "-m", "venv", VENV_DIR], check=True)
        print(f"{BLUE}[+] Sparta virtual environment created{RESET}")

        # Step 2: Activate the virtual environment and install requirements
        subprocess.run([f"{VENV_DIR}/bin/pip", "install", "-r", f"{SPARTA_DIR}/requirements.txt"], check=True)
        print(f"{BLUE}[+] Pip requirements installed{RESET}")

        # Step 3: make sparta available system-wide
        subprocess.run(['sudo', 'bash', '-c', "echo '#!/bin/bash' > /usr/bin/sparta"], check=True)
        subprocess.run(['sudo', 'bash', '-c', "echo 'cd /home/kali/tools/sparta/ && /usr/bin/env python3 sparta.py' >> /usr/bin/sparta"], check=True)
        print(f"{GREEN}[+] sparta tool now available system-wide by typing : sparta{RESET}")

        # Final instruction message
        print(f"\n{GREEN}Installation complete!{RESET}\n")
        print("To start using Sparta, follow these instructions:\n")
        print(f"1. {GREEN}Navigate to the Sparta directory:{RESET} cd {SPARTA_DIR}\n")
        print(f"2. {GREEN}Activate the virtual environment:{RESET} source {VENV_DIR}/bin/activate\n")
        print(f"3. {GREEN}Run the Sparta script directly from the directory:{RESET} python sparta.py\n")
        print(f"3. {GREEN}OR"}
        print(f"3. {GREEN}Run sparta to keep running and freeing your terminal for other commands, use nohup::{RESET} nohup sparta > sparta.log 2>&1 &\n")
        print(f"4. {GREEN}When done, deactivate the virtual environment:{RESET} deactivate\n")

# Setup configuration
setup(
    name="sparta",
    version="1.0.0",
    description="Sparta installation script",
    packages=[],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
