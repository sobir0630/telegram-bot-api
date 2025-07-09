import requests
import settings

enpoint = 'getMe'
url = f'{settings.BASE_URL}/{enpoint}'
reponse = requests.get(url)

data = reponse.json()
print(data)
