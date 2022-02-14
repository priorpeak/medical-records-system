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
    member_id = models.CharField(max_length=30)
    member_name = models.CharField(max_length=60)
