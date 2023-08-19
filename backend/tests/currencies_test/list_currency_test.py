from collections import OrderedDict

import pytest
from django.urls import reverse
from rest_framework import status

from tests.factories import CurrencyRateFactory


@pytest.mark.django_db()
class TestListSubCategoryView:
    url = reverse('currencies:currencies')

    def test_correct_return_data_keys(self, client):
        CurrencyRateFactory.create_batch(5)

        response = client.get(self.url)

        data = response.data[0]

        assert list(data.keys()) == ['id', 'currency', 'date', 'value']
        assert list(data.get('currency').keys()) == ['id', 'char_code', 'name']

    def test_correct_return_status_code(self, client):
        CurrencyRateFactory.create_batch(5)

        response = client.get(self.url)

        assert response.status_code == status.HTTP_200_OK

    def test_correct_data_type(self, client):
        CurrencyRateFactory.create_batch(5)

        response = client.get(self.url)

        data = response.data[0]

        assert [type(elem) for elem in data.values()] == [int, OrderedDict, str, str]
        assert [type(elem) for elem in data.get('currency').values()] == [int, str, str]

    def test_date_filter(self, client):
        rates = CurrencyRateFactory.create_batch(5)

        date = rates[0].date

        response = client.get(f'{self.url}?date={date}')

        assert response.data[0].get('date') == date
        assert len(response.data) == 1
