from collections.abc import Sequence
from django.contrib import admin
from django.http import HttpRequest
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        all_fields = [field for field in User._meta.get_fields()]
        valid_fields = [
            field.name for field in all_fields if not field.related_model
        ]
        valid_fields.sort()
        return valid_fields
    
admin.site.register(User, UserAdmin)