import requests

# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# check the tg bot api docs

def send_message(TOKEN, chat_id, message):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(url)

    return response.status_code

