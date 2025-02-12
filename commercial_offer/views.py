from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, CommercialOffer
from .forms import ProductForm, CommercialOfferForm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
import os

# ✅ Қаріпті тіркеу
FONT_PATH = "C:/Windows/Fonts/arial.ttf"  # Windows үшін
# FONT_PATH = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"  # Linux үшін
pdfmetrics.registerFont(TTFont("Arial", FONT_PATH))

# Басты бет (home)
def home(request):
    products = Product.objects.all()  # Барлық тауарларды шығару
    return render(request, 'home.html', {'products': products})

# Тауар қосу функциясы
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()  # Тауарды сақтау
            return redirect('generate_pdf', product_id=product.id)  # Тауар қосылған соң PDF генерациялау бетіне жіберу
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# Тауар таңдау функциясы
def choose_product(request):
    products = Product.objects.all()  # Барлық енгізілген тауарларды шығару
    return render(request, 'choose_product.html', {'products': products})

# Ұсыныс жасау
def create_offer(request):
    if request.method == 'POST':
        form = CommercialOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ұсыныс жасалған соң, басты бетке оралу
    else:
        form = CommercialOfferForm()
    return render(request, 'create_offer.html', {'form': form})

# ✅ PDF генерациялау функциясы (Arial қарпімен)
def generate_pdf(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    buffer = BytesIO()  # PDF құру үшін буфер
    p = canvas.Canvas(buffer)
    
    # PDF мазмұны
    p.setFont("Arial", 16)
    p.drawString(100, 750, "Тауар туралы ақпарат")
    
    p.setFont("Arial", 12)
    p.drawString(100, 720, f"Атауы: {product.name}")
    p.drawString(100, 700, f"Сипаттама: {product.description}")
    p.drawString(100, 680, f"Бағасы: {product.price} ₸")
    p.drawString(100, 660, f"Саны: {product.quantity}")  # Quantity қосылды

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{product.name}.pdf"'
    
    return response
