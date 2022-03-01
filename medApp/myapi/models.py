from django.db import models
import uuid

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.UUIDField(
        'UID',
        primary_key = True,
        default = uuid.uuid4,
        editable = False
        )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    pcp = models.CharField('PCP', max_length=30)
    SEXES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    sex = models.CharField(max_length=1, choices=SEXES)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    insurance_company = models.CharField(max_length=30)
    member_id = models.CharField(max_length=30)
    member_name = models.CharField(max_length=60)
    credit_card_number = models.CharField(max_length=16)
    credit_card_expiration = models.CharField('Expiration date', max_length=5)
    credit_card_cvv = models.CharField('CVV', max_length=3)

class Medical_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_medications = models.CharField(max_length=30)
    family_med_history = models.CharField('Family Medical History', max_length=60)
    past_meds = models.CharField('Past Medications', max_length=60)
    allergies = models.CharField(max_length=60)

class Roles(models.Model):
    role = models.CharField(max_length=30)

class User_Roles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ROLES = (
        (1, 'Patient'),
        (2, 'Nurse'),
        (3, 'Doctor'),
        (4, 'Admin'),
        (5, 'Family Member')
    )
    role_id = models.IntegerField(choices=ROLES)
    deleted_bool = models.BooleanField()
    time_modified = models.TimeField(auto_now=True)

class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.FloatField()
    blood_pressure = models.FloatField()
    pulse = models.IntegerField()
    blood_oxygen = models.CharField(max_length=4)
    weight = models.IntegerField()
    height = models.FloatField()

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=60)
    date_of_purchase = models.DateField()
    MAC_address = models.CharField('MAC Address', max_length=30)
