from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="carts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Cart ({self.id}) for {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products"
    )
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart {self.cart.id}"