from py_quote.animechan_api_client import get_quote
from tg_api_client import send_message
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN') 
chat_id = os.getenv('TELEGRAM_CHAT_ID')

if __name__ == "__main__":

    try:
        quote = get_quote()
        if quote:
            send_message(TOKEN=TOKEN, chat_id=chat_id, message=quote)
        else:
            send_message('something went wrong')
    except Exception as e:
        print(e)
        

    