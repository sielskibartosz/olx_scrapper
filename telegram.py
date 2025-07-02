import os
import requests
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe z pliku .env (tylko raz na start programu)
load_dotenv()

class Telegram:
    def __init__(self):
        # Pobieramy token i chat_id ze zmiennych środowiskowych
        self.TOKEN = os.getenv("TOKEN")
        self.CHAT_ID = os.getenv("CHAT_ID")
        if not self.TOKEN or not self.CHAT_ID:
            raise ValueError("Brak TELEGRAM TOKEN lub CHAT_ID w zmiennych środowiskowych")

    def send_message(self, text: str) -> bool:
        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage"
        payload = {
            'chat_id': self.CHAT_ID,
            'text': text
        }
        response = requests.post(url, data=payload)
        return response.ok


