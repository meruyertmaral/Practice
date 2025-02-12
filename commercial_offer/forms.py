from django import forms
from .models import CommercialOffer, Product

class CommercialOfferForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),  # Тек енгізілген тауарларды таңдауға мүмкіндік береді
        empty_label="Тауарды таңдаңыз", 
        label="Таңдаулы тауар"
    )

    class Meta:
        model = CommercialOffer
        fields = ['client', 'product', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Саны 0-ден үлкен болуы керек.")
        return quantity

class ProductForm(forms.ModelForm):
    quantity = forms.IntegerField(
        min_value=1,
        label="Саны",
        help_text="Тауар санын енгізіңіз"
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']  # "quantity" қосылды

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Баға 0-ден үлкен болуы керек.")
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Саны 0-ден үлкен болуы керек.")
        return quantity
