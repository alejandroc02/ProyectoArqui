from django.contrib import admin
from .models import Client, ClientProfile, Employee

admin.site.register(Client)
admin.site.register(ClientProfile)
admin.site.register(Employee)
