from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'username': {'required': False},
            'password': {'write_only': True, 'required': False}
        }
        
    def update(self, instance, validated_data):
        pwd = validated_data.pop("password", None)
        if pwd:
            instance.set_password(pwd)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance