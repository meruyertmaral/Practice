from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Бұл негізгі бетке бағыттайды
    path('create/', views.create_offer, name='create_offer'),
    path('offer/<int:pk>/', views.offer_detail, name='offer_detail'),
]
