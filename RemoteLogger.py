import requests
import datetime

class RemoteLogger:
    def __init__(self, endpoint_url):
        self.url = endpoint_url

    def log(self, service, event, details):
        log_data = {
            "event": event,
            "details": details,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "service": service
        }

        try:
            response = requests.post(self.url, json=log_data)
            if response.status_code != 200:
                print(f"Log failed: {response.text}")
        except Exception as e:
            print(f"Failed to send log: {e}")
