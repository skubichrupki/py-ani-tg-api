import requests

def get_quote():
    url = "https://animechan.io/api/v1/quotes/random"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            json = response.json()
            content = json['data']['content']
            anime_name = json['data']['anime']['name']
            character_name = json['data']['character']['name']

            result = f'{content} ~ {character_name} | {anime_name}'
            return result
        else:
            return response.status_code
    except Exception as e:
        return str(e)