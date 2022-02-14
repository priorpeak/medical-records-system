from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer, UserSerializer
from .models import Hero, User

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('last_name')
    serializer_class = UserSerializer