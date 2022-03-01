from rest_framework import serializers
from .models import Hero, User, Billing, Medical_History, Roles, User_Roles, Measurements, Device

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'address', 'pcp', 'sex')

class BillingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Billing
        fields = ('user', 'insurance_company', 'member_id', 'member_name', 'credit_card_number', 'credit_card_expiration', 'credit_card_cvv')

class Medical_HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medical_History
        fields = ('user', 'current_medications', 'family_med_history', 'past_meds', 'allergies')

class RolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'role')

class User_RolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Roles
        fields = ('user', 'role_id', 'deleted_bool', 'time_modified')

class MeasurementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurements
        fields = ('user', 'temperature', 'blood_pressure', 'pulse', 'blood_oxygen', 'weight', 'height')

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('user', 'type', 'date_of_purchase', 'MAC_address')