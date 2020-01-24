import requests
from rest_framework.parsers import JSONParser

from curr_api.models import Currency

# fixer.io API
URL = "http://data.fixer.io/api/"
ACCESS_KEY = "ecf4d5e2396223857dc9a9f45d59f7f7"


def fixer_request():
    params = {'access_key': ACCESS_KEY,
              'symbols': "EUR, CZK,PLN,USD"}
    request = requests.get(url=URL + 'latest', params=params)

    if request.status_code != requests.codes.ok:
        print("error")
    else:
        data = request.json()
        rates = data['rates']
        for code in rates:
            try:
                item = Currency.objects.get(code=code)
            except Currency.DoesNotExist:
                Currency.objects.create(rate=rates[code], code=code)
            else:
                item.rate = rates[code]
                item.save()


def exchange_rate(data):
    from_currency = Currency.objects.get(code=data['from_curr'])
    to_currency = Currency.objects.get(code=data['to_curr'])
    amount = round(data['from_amount'] * to_currency.rate / from_currency.rate, 2)
    return amount
