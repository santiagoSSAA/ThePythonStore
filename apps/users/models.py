from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class User(AbstractUser):
    groups = models.ManyToManyField(
        Group, related_name='customuser_set', blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_permissions_set', blank=True
    )
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