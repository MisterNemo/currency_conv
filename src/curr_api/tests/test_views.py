import json
import pytest

from django.urls import reverse
from rest_framework.test import APIRequestFactory

from curr_api.views import CurrencyView
from curr_api.models import Currency

from curr_api.utils import exchange_rate


@pytest.fixture
def factory():
    return APIRequestFactory()


def test_currency_list(factory, db):
    request = factory.get('/api/v1/currencies/')
    response = CurrencyView.as_view()(request)

    assert response.status_code == 200


def test_exchange(factory, db):
    from_currency = Currency.objects.create(
        code='KZT',
        rate=427.79
    )

    to_currency = Currency.objects.create(
        code='RUB',
        rate=70.41
    )

    from_amount = 122

    PARAMS = {
        'from_curr': from_currency.code,
        'to_curr': to_currency.code,
        'from_amount': from_amount
    }

    request = factory.get(
        url = '/api/v1/exchange/',
        params=PARAMS
    )

    response = CurrencyView.as_view()(request)

    body = response.data

    test_amount = exchange_rate(PARAMS)

    assert body['amount'] == test_amount
