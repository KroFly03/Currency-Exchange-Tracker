from rest_framework import generics

from currencies.filters import CurrencyRateFilter
from currencies.serializers import CurrencyRateSerializer
from currencies.models import CurrencyRate


class CurrencyRateView(generics.ListAPIView):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer
    filterset_class = CurrencyRateFilter
