import requests
import settings

def get_me():
    endpoint = 'getMe'
    url = f'{settings.BASE_URL}/{endpoint}'
    reponse = requests.get(url)

    return reponse.json()

def get_updates():
    endpoint = 'getUpdates'
    url = f'{settings.BASE_URL}/{endpoint}'
    reponse = requests.get(url)

    return reponse.json()


def send_message(user_id, text):
    endpoint = 'sendMessage'
    url = f'{settings.BASE_URL}/{endpoint}'
    
    payload = {
        'chat_id': user_id,
        'text': text
    }
    requests.get(url, data=payload)

def send_contact(user_id, phone_number, first_name):
    pass

user_id = 5895818044
text = 'salom men ZiyoQuiz Botman'
send_message(user_id, text)
