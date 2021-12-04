from rest_framework import serializers
# import the user model
from .models import User
# Create a class that links the User with its serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')
