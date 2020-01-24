import pytest

from curr_api.models import Currency


@pytest.mark.django_db
class TestModels:

    def test_currency_save(self):
        currency = Currency.objects.create(
            code = 'KZT',
            rate = 428.23
        )
        assert currency.code == 'KZT'
        assert currency.rate == 428.23