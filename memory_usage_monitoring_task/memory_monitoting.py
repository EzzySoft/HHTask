import time

import psutil
import requests

URL_API = "https://testservice.com/api/alarm"

MEMORY_THRESHOLD_PERCENT = 85
MESSAGES_COOLDOWN_SECONDS = 10


def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD_PERCENT:
        send_alarm()
        print(f"Waiting {MESSAGES_COOLDOWN_SECONDS} seconds...")
        time.sleep(MESSAGES_COOLDOWN_SECONDS)


def send_alarm():
    data = {
        "message": "Memory consumption has exceeded the threshold!",
        "memory_percent": psutil.virtual_memory().percent
    }

    try:
        response = requests.post(URL_API, json=data, timeout=10)
        if response.status_code == 200:
            print("Alarm message sent")
        else:
            print(f"Error while sending message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Unexpected error while sending message: {str(e)}")


if __name__ == "__main__":
    while True:
        check_memory_usage()
