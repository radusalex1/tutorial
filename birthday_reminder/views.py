from attr import asdict
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers

from birthday_reminder.serializers import ContactSerializer, GroupSerializer
from .models import *
import datetime

# Create your views here.
@api_view(('GET',))
def birthday_reminder(request):
    try:
        contacts = Contact.objects.get(birth_date__day = datetime.datetime.now().day,birth_date__month = datetime.datetime.now().month,active=True)
        return JsonResponse(contacts)
    except Contact.DoesNotExist:
        return HttpResponse('Nu e ziua nimanui')
    except Exception as e:
        return HttpResponse(e)
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class = GroupSerializer