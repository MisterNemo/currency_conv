from rest_framework.views import APIView
from rest_framework.response import Response

from curr_api.serializer import CurrencySerializer
from curr_api.serializer import ExchangeRateSerializer
from curr_api.models import Currency as CurrencyModel

from curr_api.utils import exchange_rate


class CurrencyView(APIView):
    def get(self, request, format=None):
        snippets = CurrencyModel.objects.all()
        serializer = CurrencySerializer(snippets, many=True)
        return Response(serializer.data)

class ExchangeView(APIView):
    def get(self, request, format=None):
        serializer = ExchangeRateSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        amount = exchange_rate(serializer.data)
        return Response({'amount': amount})
