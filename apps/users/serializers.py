from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from django.core.validators import FileExtensionValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)
    
    photo = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], 
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'photo', 'password')

    def validate_password(self, value):
        return make_password(value)
    

class GroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, required=True)

    class Meta:
        model = Group
        fields = '__all__'