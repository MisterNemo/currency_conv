from django.conf.urls import url

from rest_framework import routers

from curr_api.views import CurrencyView
from curr_api.views import ExchangeView

router = routers.SimpleRouter()

api_urlpatterns = [
    url(r'currencies/', CurrencyView.as_view()),
    url(r'exchange/', ExchangeView.as_view()),

]

api_urlpatterns += router.urls
