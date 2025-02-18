from animechan_api_client import AnimechanApi
from telegram_api_client import TelegramApi
from dotenv import load_dotenv
import os

load_dotenv()

class SendManager():
    def __init__(self):
        self.token = os.getenv('TELEGRAM_TOKEN') 
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.url = 'https://animechan.io/api/v1/quotes/random'

    def api_animechan(self):
        api = AnimechanApi(url=self.url)
        result = api.get_quote()
        return result

    def api_telegram(self, e=None):
        text = e if e else self.api_animechan()
        api = TelegramApi(TOKEN=self.token, chat_id=self.chat_id, text=text)
        response = api.send_text()
        return response

if __name__ == "__main__":
    send_manager = SendManager()
    try:
        response = send_manager.api_telegram()
    except Exception as e:
        response = send_manager.api_telegram(str(e))
        print(f'error: {e}')