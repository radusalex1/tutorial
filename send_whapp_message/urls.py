from django.urls import path

from . import views

urlpatterns = [
    path('send_whapp_message', views.send_whapp_message, name='send_whapp_message'),
    path('send_sms',views.send_sms,name = 'send_sms')
]