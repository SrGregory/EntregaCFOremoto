from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from indicator.models import Uf
from indicator.serializers import UfSerializer


class UfListView(generics.ListAPIView):
    queryset = Uf.objects.all()
    serializer_class = UfSerializer
    permission_classes = (AllowAny,)
