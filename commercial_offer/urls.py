from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Басты бет
    path('add/', views.add_product, name='add_product'),  # Тауар қосу
    path('choose/', views.choose_product, name='choose_product'),  # Тауар таңдау
    path('offer/', views.create_offer, name='create_offer'),  # Ұсыныс жасау
    path('pdf/<int:product_id>/', views.generate_pdf, name='generate_pdf'),  # ✅ PDF жүктеу маршруты
]
