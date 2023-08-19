from django.db import models


class Currency(models.Model):
    char_code = models.CharField(verbose_name='Код', max_length=3)
    name = models.CharField(verbose_name='Название', max_length=50)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        unique_together = ('char_code', 'name')

    def __str__(self):
        return self.name


class CurrencyRate(models.Model):
    currency = models.ForeignKey(Currency, verbose_name='Валюта', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата сбора данных', auto_now_add=True)
    value = models.DecimalField(verbose_name='Курс', max_digits=10, decimal_places=4)

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы Валют'
        unique_together = ('currency', 'date')

    def __str__(self):
        return f"{self.currency.char_code} - {self.date}"
