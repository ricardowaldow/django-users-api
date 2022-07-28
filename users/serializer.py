""" Users App Serializers """
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """ User serializer class"""
    hash = serializers.ReadOnlyField()
    class Meta:
        """User Serializer Meta class"""
        model = User
        exclude = ['id','password']
