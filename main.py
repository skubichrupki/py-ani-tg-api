from animechan_api_client import AnimechanApi
from telegram_api_client import TelegramApi
from dotenv import load_dotenv
import os

def api_animechan():
    url = 'https://animechan.io/api/v1/quotes/random'
    api = AnimechanApi(url=url)
    result = api.get_quote()
    return result

def api_telegram(e=None):
    load_dotenv()
    TOKEN = os.getenv('TELEGRAM_TOKEN') 
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    text = e if e else api_animechan()
    api = TelegramApi(TOKEN=TOKEN, chat_id=chat_id, text=text)
    response = api.send_text()
    return response

if __name__ == "__main__":

    try:
        response = api_telegram()
    except Exception as e:
        response = api_telegram(str(e))
        print(f'error: {e}')