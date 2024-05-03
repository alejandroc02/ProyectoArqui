from django.db import models
from Usuario.models import Client


class CreditCardProfile(models.TextChoices):
    STANDARD = 'STANDARD'
    GOLD = 'GOLD'
    SILVER = 'SILVER'
    BLACK = 'BLACK'

class Franchise(models.TextChoices):
    MASTERCARD = 'MASTERCARD'
    VISA = 'VISA'
    
class CreditCard(models.Model):
    creditLimit = models.IntegerField()
    creditCardProfile = models.CharField(choices=CreditCardProfile.choices, max_length=10, default=CreditCardProfile.STANDARD)
    franchise = models.CharField(choices=Franchise.choices, max_length=10, default=Franchise.MASTERCARD)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name
    
