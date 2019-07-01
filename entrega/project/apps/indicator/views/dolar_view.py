from rest_framework import generics
from rest_framework.permissions import AllowAny

from indicator.models import Dolar
from indicator.serializers import DolarSerializer


class DolarListView(generics.ListCreateAPIView):
    queryset = Dolar.objects.all()
    serializer_class = DolarSerializer
    permission_classes = (AllowAny,)
