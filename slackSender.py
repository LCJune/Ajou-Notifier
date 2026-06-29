import os
import requests
class slackSender:
    def __init__(self):
        self.webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

    def send_message(self, message):
        payload = {
            "text": message,
            "username": "AJOU Notifier"
        }
        response = requests.post(self.webhook_url, json=payload)
        
        if response.status_code != 200:
            raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
        
