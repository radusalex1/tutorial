from django.urls import path

from . import views

urlpatterns = [
    path("send_message", views.send_whapp_message, name="send_whapp_message"),
]