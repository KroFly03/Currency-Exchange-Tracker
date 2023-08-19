from rest_framework import generics

from backend.currencies.serializers import CurrencyRateSerializer
from currencies.models import CurrencyRate


class CurrencyRateView(generics.ListAPIView):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer

