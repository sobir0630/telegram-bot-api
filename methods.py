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
    endpoint = 'sendContact'
    url = f'{settings.BASE_URL}/{endpoint}'
    
    payload = {
        'chat_id': user_id,
        'phone_number': phone_number,
        'first_name': first_name
    }
    requests.get(url, data=payload)


user_id = 1258594598
phone_number = '+998991234567'
first_name = "Ali"
send_contact(user_id, phone_number, first_name)

