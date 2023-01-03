from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent.parent

subprocess.run(["pip3", "freeze", ">", "requirements.txt"])
