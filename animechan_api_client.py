import requests

class AnimechanApi(): 
    url = None

    def __init__(self, url):
        self.url = url

    def get_quote(self):
        url = self.url
        
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