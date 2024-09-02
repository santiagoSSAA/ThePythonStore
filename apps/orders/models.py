from django.db import models
from django.contrib.auth import get_user_model
from apps.payments.models import Payment
from apps.products.models import Product

User = get_user_model()

# Create your models here.
class OrderStatus(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders"
    )
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    payment = models.ManyToManyField(Payment, on_delete=models.RESTRICT, related_name="orders")
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products"
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
