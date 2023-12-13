from django.conf import settings
from django.http import HttpResponse
import pywhatkit as kit
from twilio.rest import Client

def send_whapp_message(request):
    account_sid = 'AC6df44d4ccc1694be926adc5a841dfe28'
    auth_token = '53b57b0cee3d98c26b4ce2b61d28796f'
    client = Client(account_sid, auth_token)

    phone_numbers = ['+40735125928']

    message = settings.MESSAGE

    for ph in phone_numbers:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'{message}',
            to=f'whatsapp:{ph}'
        )

    return HttpResponse("Hello, world. You're at the polls index.")