from django.shortcuts import render
from rest_framework import viewsets
from django.http.response import JsonResponse
# import the User model and serializer
from .serializers import UserSerializer
from .models import User
import django_filters.rest_framework

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']

    def get_serializer(self, *args, **kwargs):
        data = None
        if "data" in kwargs:
            data = kwargs["data"]
        # check if many is required
        if isinstance(data, list):
                kwargs["many"] = True

        return super(UserViewSet, self).get_serializer(*args, **kwargs)
