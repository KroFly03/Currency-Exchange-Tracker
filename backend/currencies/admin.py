from django.contrib import admin

from currencies.models import Currency, CurrencyRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('char_code', 'name')
    search_fields = ('name',)


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('get_currency_name', 'value', 'date')
    search_fields = ('date',)

    def get_currency_name(self, obj):
        return obj.currency.name

    get_currency_name.short_description = 'Валюта'
