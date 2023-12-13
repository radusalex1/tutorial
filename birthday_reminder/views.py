from attr import asdict
from django.http import HttpResponse
from .models import *
import datetime

# Create your views here.
def birthday_reminder(request):
    try:
        contacts = Contact.objects.get(birth_date__day = datetime.datetime.now().day,birth_date__month = datetime.datetime.now().month,active=True)
        return HttpResponse(contacts)
    except Contact.DoesNotExist:
        return HttpResponse("Nu e ziua nimanui")
    except Exception as e:
        return HttpResponse(e)