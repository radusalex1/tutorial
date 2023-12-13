from django.urls import path

from . import views

urlpatterns = [
    path("today_births", views.birthday_reminder, name="today_births"),
]