import subprocess
import time

PRUNE_FREQUENCY = 2000

def main():
    while True:
        subprocess.call('docker system prune -f --filter "until=30m"', shell=True) 
        time.sleep(PRUNE_FREQUENCY)


if __name__ == "__main__":
    main()
