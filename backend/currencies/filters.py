import django_filters
from django_filters import filters

from currencies.models import CurrencyRate


class CurrencyRateFilter(django_filters.FilterSet):
    date = filters.CharFilter(field_name='date', lookup_expr='exact')

    class Meta:
        model = CurrencyRate
        fields = ('date',)
