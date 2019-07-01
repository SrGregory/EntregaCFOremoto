from rest_framework import serializers

from indicator.models import Dolar


class DolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dolar
        fields = '__all__'
