from rest_framework import serializers

from currencies.models import CurrencyRate, Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class CurrencyRateSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = CurrencyRate
        fields = '__all__'
