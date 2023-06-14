from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from django.core.validators import FileExtensionValidator

class PermissionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        permissions = instance.permissions.all()
        group_names = [group.name for group in permissions]
        representation['permissions'] = group_names
        return representation



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)
    
    photo = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], 
        required=False
    )

    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    permissions = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'photo', 'password', 'groups', 'permissions')


    def validate_password(self, value):
        return make_password(value)
    

    def get_permissions(self, obj):
        permissions = obj.user_permissions.all()
        return [permission.name for permission in permissions]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        groups = instance.groups.all()
        group_names = [group.name for group in groups]
        representation['groups'] = group_names
        # Eliminar la contraseña del diccionario de representación
        representation.pop('password', None)
        representation.pop('permissions', None)
        return representation