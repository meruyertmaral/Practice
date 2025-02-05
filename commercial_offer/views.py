from django.shortcuts import render, redirect
from .models import CommercialOffer
from .forms import CommercialOfferForm

def home(request):
    return render(request, 'home.html')
def create_offer(request):
    if request.method == 'POST':
        form = CommercialOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.calculate_total_price()
            offer.save()
            return redirect('offer_detail', pk=offer.pk)
    else:
        form = CommercialOfferForm()
    return render(request, 'create_offer.html', {'form': form})

def offer_detail(request, pk):
    offer = CommercialOffer.objects.get(pk=pk)
    return render(request, 'offer_detail.html', {'offer': offer})
