from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer, UserSerializer, BillingSerializer, Medical_HistorySerializer, RolesSerializer, User_RolesSerializer, MeasurementsSerializer, DeviceSerializer
from .models import Hero, User, Billing, Medical_History, Roles, User_Roles, Measurements, Device

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('last_name')
    serializer_class = UserSerializer

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all().order_by('user')
    serializer_class = BillingSerializer

class Medical_HistoryViewSet(viewsets.ModelViewSet):
    queryset = Medical_History.objects.all().order_by('user')
    serializer_class = Medical_HistorySerializer

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all().order_by('role')
    serializer_class = RolesSerializer

class User_RolesViewSet(viewsets.ModelViewSet):
    queryset = User_Roles.objects.all().order_by('user')
    serializer_class = User_RolesSerializer

class MeasurementsViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all().order_by('user')
    serializer_class = MeasurementsSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('user')
    serializer_class = DeviceSerializer