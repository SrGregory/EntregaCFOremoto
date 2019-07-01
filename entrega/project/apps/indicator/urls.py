from django.urls import path

from indicator.views import CurrencyView, UfListView, DolarListView

urlpatterns = [
    path('currency/', CurrencyView.as_view(), name = 'currency'),
    path('currency/uf/', UfListView.as_view(), name= 'uflist'),
    path('currency/dolar/', DolarListView.as_view(), name = 'dolarlist'),
    ]

