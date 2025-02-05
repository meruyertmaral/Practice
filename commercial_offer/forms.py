from django import forms
from .models import CommercialOffer

class CommercialOfferForm(forms.ModelForm):
    class Meta:
        model = CommercialOffer
        fields = ['client', 'product', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Саны 0-ден үлкен болуы керек.")
        return quantity
