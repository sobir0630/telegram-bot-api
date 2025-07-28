import requests
from settings import TOKEN

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

params = {
    'chat_id': 1258594598,
    'text': "salom"
}

r = requests.get(url=url, params=params)

print(r.status_code)
