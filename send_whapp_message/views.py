import datetime
from django.conf import settings
from django.http import HttpResponse
import pywhatkit as kit
from twilio.rest import Client
from mailersend import sms_sending
from birthday_reminder.models import Contact

def send_whapp_message(request):
    account_sid = settings.ACCCOUNT_SID
    auth_token = settings.AUTH_TOKEN
    client = Client(account_sid, auth_token)

    phone_numbers = settings.PHONE_NUMBERS

    try:
        contacts = Contact.objects.get(birth_date__day = datetime.datetime.now().day,birth_date__month = datetime.datetime.now().month,active=True)
        message = contacts
    except Contact.DoesNotExist:
        message = 'Nu e ziua nimanui'
    except Exception as e:
        return HttpResponse(e)
    

    for ph in phone_numbers:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'{message}',
            to=f'whatsapp:{ph}'
        )

    return HttpResponse("Hello, world. You're at the polls index.")

def send_sms(request):
    api_key = "API key here"

    mailer = sms_sending.NewSmsSending(api_key)

    # Number belonging to your account in E164 format
    number_from = "+11234567890"

    #You can add up to 50 recipient numbers
    numbers_to = [
        "+11234567891",
        "+11234567892"
    ]
    text = "This is the text content"

    print(mailer.send_sms(number_from, numbers_to, text))