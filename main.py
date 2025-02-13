from animechan_api_client import get_quote
from telegram_api_client import send_text
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN') 
chat_id = os.getenv('TELEGRAM_CHAT_ID')

if __name__ == "__main__":

    try:
        text = get_quote()
        if text:
            res = send_text(TOKEN=TOKEN, chat_id=chat_id, text=text)
            print(res)
        else:
            send_text('something went wrong')
    except Exception as e:
        print(e)
        

    