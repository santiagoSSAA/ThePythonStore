from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
    )
    email = models.EmailField(unique=True, help_text="Required. Inform a valid email address")
    first_name = models.CharField(max_length=30, blank=True, help_text="Optional.")
    last_name = models.CharField(max_length=30, blank=True, help_text="Optional.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"