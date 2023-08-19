from datetime import datetime

import requests
from django.core.management import BaseCommand
from django.db import transaction

from currencies.models import Currency, CurrencyRate
from currency_exchange_tracker.settings import UPLOAD_URL


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        try:
            data = requests.get(UPLOAD_URL).json()

            for char_code, currency_data in data['Valute'].items():
                with transaction.atomic():
                    currency, _ = Currency.objects.get_or_create(
                        char_code=char_code,
                        defaults={'name': currency_data['Name']}
                    )

                    date = datetime.now().date()

                    rate, created = CurrencyRate.objects.get_or_create(
                        currency=currency,
                        value=currency_data['Value'],
                        date=date
                    )

                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f'Успешно добавлено {currency} на {date}.'))
                    else:
                        self.stdout.write(self.style.WARNING(f'{currency} на {date} уже добавлено.'))
        except Exception as ex:
            self.stdout.write(self.style.ERROR(f'Ошибка при выполнении команды: {str(ex)}.'))
