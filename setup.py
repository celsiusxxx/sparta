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

        # # Step 1: Remove previous installation if it exists
        # if os.path.exists(SPARTA_DIR):
        #     subprocess.run(["rm", "-rf", SPARTA_DIR], check=True)
        #     print(f"{BLUE}[+] Removed any previous installation{RESET}")

        # # Step 2: Clone the Sparta repository
        # subprocess.run(["git", "clone", "https://github.com/celsiusxxx/sparta.git", SPARTA_DIR], check=True)
        # print(f"{BLUE}[+] Sparta GitHub repository cloned{RESET}")

        # Step 3: Create virtual environment
        subprocess.run(["/usr/bin/env", "python", "-m", "venv", VENV_DIR], check=True)
        print(f"{BLUE}[+] Sparta virtual environment created{RESET}")

        # Step 4: Activate the virtual environment and install requirements
        subprocess.run([f"{VENV_DIR}/bin/pip", "install", "-r", f"{SPARTA_DIR}/requirements.txt"], check=True)
        print(f"{BLUE}[+] Pip requirements installed{RESET}")

        # Final instruction message
        print(f"\n{GREEN}Installation complete!{RESET}\n")
        print("To start using Sparta, follow these instructions:\n")
        print(f"1. {GREEN}Navigate to the Sparta directory:{RESET}")
        print(f"   cd {SPARTA_DIR}\n")
        print(f"2. {GREEN}Activate the virtual environment:{RESET}")
        print(f"   source {VENV_DIR}/bin/activate\n")
        print(f"3. {GREEN}Run the Sparta script:{RESET}")
        print(f"   python sparta.py\n")
        print(f"4. {GREEN}When done, deactivate the virtual environment:{RESET}")
        print("   deactivate\n")

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
