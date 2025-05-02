import base64
import os

# Code obfuscation (renaming variables)
a = "files.log"
b = "key.bin"
c = base64.b64encode(b"Secret data").decode('utf-8')

def run():
    print(f"Logging to: {a}")
    print(f"Key saved as: {b}")
    print(f"Base64 encoded data: {c}")

run()

# Persistence: Add a cron job to run on system reboot (Linux)
def add_cron_job():
    cron_job = "@reboot /usr/bin/python3 /path/to/script.py\n"  # Update path to your script
    with open('/etc/crontab', 'a') as cron:
        cron.write(cron_job)
    print("Cron job added for persistence.")

add_cron_job()