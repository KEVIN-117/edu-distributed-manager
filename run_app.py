import os
import platform
import subprocess
import sys
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME")
PORT = os.getenv("PORT", "8000")

def run_celery():
    system = platform.system().lower()

    cmd = ["celery", "-A", PROJECT_NAME, "worker", "-l", "info"]

    if system == "windows":
        cmd += ["--pool=solo"]
    else:
        cmd += ["--pool=prefork"]
    print(f'Running Celery with command: {" ".join(cmd)}')
    subprocess.call(cmd)

def main():
    run_celery()


if __name__ == "__main__":
    sys.exit(main())
