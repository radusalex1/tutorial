from django.urls import include, path
from rest_framework.routers import DefaultRouter,SimpleRouter
from . import views

urlpatterns = [
    path('today_births', views.birthday_reminder, name='today_births')
]