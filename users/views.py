from django.shortcuts import render
from users.models import Sp_user
from rest_framework import viewsets
from users.serializers import UserSerializers


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Sp_user.objects.all()
    serializer_class = UserSerializers
