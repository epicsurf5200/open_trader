"""Post messages to Discord via a webhook URL."""
import os

import requests


def send(message: str) -> None:
    """Post `message` to the Discord webhook at DISCORD_WEBHOOK_URL."""
    url = os.environ["DISCORD_WEBHOOK_URL"]
    response = requests.post(url, json={"content": message}, timeout=10)
    response.raise_for_status()
