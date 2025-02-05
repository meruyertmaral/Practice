from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('offers/', include('commercial_offer.urls')),
    path('', include('commercial_offer.urls')),  # Бұл негізгі бетке бағыттайды
]
