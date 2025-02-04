# myproject/urls.py
from django.contrib import admin
from django.urls import path
from . import views  # views файлы импортталды

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # home көрінісі қосылды
]
