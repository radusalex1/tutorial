# birthday_reminder/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime

@shared_task
def send_birthday_reminder():
    today = datetime.now().date()
    print("hello")
