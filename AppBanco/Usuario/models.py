from django.db import models
from Document.models import Document # o pude ser from AppBanco import Document


class ClientProfile(models.Model):
    profession = models.CharField(max_length=255)
    ciiu_economic_activity = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    income = models.CharField(max_length=255)
    expense = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.id)

class Client(models.Model):
    name = models.CharField(max_length=255, null=True)
    email= models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    city= models.CharField(max_length=255, null=True)
    cell_number = models.CharField(max_length=255, null=True)
    client_profile = models.OneToOneField(ClientProfile, on_delete=models.CASCADE,null=True) 
    documents = models.ForeignKey(Document, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.id)
    

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email= models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.id)