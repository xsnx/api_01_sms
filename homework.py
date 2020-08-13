import os
import time
import requests
from twilio.rest import Client
from dotenv import load_dotenv


def get_status(user_id):
    load_dotenv()
    vk_token = os.getenv('vk_token')
    params = {
        'v': '5.122',
        'access_token': vk_token,
        'user_ids': user_id,
        'fields': 'online',
    }
    vk_api_url = 'https://api.vk.com/method/'
    api_method = 'users.get'
    response = requests.post(f'{vk_api_url}{api_method}', params=params).json()
    return response['response'][0]['online']


def sms_sender(sms_text):
    load_dotenv()
    account_SID = os.getenv('account_SID')
    token = os.getenv('Token_twilio')
    NUMBER_FROM = os.getenv('NUMBER_FROM')
    NUMBER_TO = os.getenv('NUMBER_TO')
    account_sid = account_SID
    auth_token = token
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=sms_text,
        from_=NUMBER_FROM,
        to=NUMBER_TO
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
