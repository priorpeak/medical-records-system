from django.contrib import admin
from .models import Hero, User, Billing, Medical_History, Roles, User_Roles, Measurements, Device

# Register your models here.
admin.site.register(Hero)
admin.site.register(User)
admin.site.register(Billing)
admin.site.register(Medical_History)
admin.site.register(Roles)
admin.site.register(User_Roles)
admin.site.register(Measurements)
admin.site.register(Device)