from rest_framework import viewsets
from .serializer import CreditCardSerializer
from .models import CreditCard

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer