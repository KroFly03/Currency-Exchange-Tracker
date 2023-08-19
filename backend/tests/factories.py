import factory.django

from pytest_factoryboy import register

from currencies.models import Currency, CurrencyRate


@register
class CurrencyFactory(factory.django.DjangoModelFactory):
    char_code = 'cur'
    name = factory.Sequence(lambda n: f'Name{n}')

    class Meta:
        model = Currency


@register
class CurrencyRateFactory(factory.django.DjangoModelFactory):
    currency = factory.SubFactory(CurrencyFactory)
    date = factory.Faker('date')
    value = 100

    class Meta:
        model = CurrencyRate
