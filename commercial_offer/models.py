from django.db import models
from django.contrib.auth.models import User  

# Клиент моделі
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

# Тауар моделі
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)  # Жаңа өріс (тауар саны)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):
        return self.name

# Коммерциялық ұсыныс моделі
class CommercialOffer(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Баға автоматты түрде есептеледі
    offer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Offer for {self.client.name} - {self.product.name}"

    def save(self, *args, **kwargs):
        # Жалпы бағаны автоматты түрде есептеу
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
