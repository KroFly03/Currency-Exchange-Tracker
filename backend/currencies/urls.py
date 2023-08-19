from django.urls import path

from currencies.views import CurrencyRateView

app_name = 'currencies'

urlpatterns = [
    path('/show_rates', CurrencyRateView.as_view(), name='currencies')
]
