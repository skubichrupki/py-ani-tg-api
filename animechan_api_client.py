import requests

def get_quote():
    url = "https://animechan.io/api/v1/quotes/random"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            json = response.json()
            quote = json['data']['content']
            anime = json['data']['anime']['name']
            character = json['data']['character']['name']

            data = f'{quote} ~ {character} | {anime}'
            return data
        else:
            return response.status_code 
    except Exception as e:
        return str(e)