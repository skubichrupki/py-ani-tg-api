import requests

# check the telegram bot api docs
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# res = requests.get(url)
# print(res._content)


def send_text(TOKEN, chat_id, text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    response = requests.get(url)

    return response.status_code

    # check if this would work
    # params = {'chat_id':chat_id, 'text':text}
    # url = 'https://api.telegram.org/bot{TOKEN}/sendMessage'
    # response = requests.get(url, params=params)
    # print(response.url)
