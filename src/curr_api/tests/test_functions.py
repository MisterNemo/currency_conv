import requests


from curr_api import utils

def test_fixer_api_request():
    params = {'access_key': utils.ACCESS_KEY,
              'symbols': "EUR, CZK,PLN,USD"}
    request = requests.get(url=utils.URL + 'latest', params=params)

    assert request.status_code == requests.codes.ok