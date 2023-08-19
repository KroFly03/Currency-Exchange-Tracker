from rest_framework import serializers

from currencies.models import CurrencyRate


class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = '__all__'
