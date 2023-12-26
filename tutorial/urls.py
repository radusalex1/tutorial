'''
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from birthday_reminder.views import ContactViewSet, GroupViewSet
from tutorial import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"contacts",ContactViewSet,basename='contacts')
router.register(r"groups",GroupViewSet,basename='groups')


urlpatterns = [
    path('api/v1/',include(router.urls)),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/message/', include('send_whapp_message.urls')),
    path('api/v1/birthday_reminder/', include('birthday_reminder.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

