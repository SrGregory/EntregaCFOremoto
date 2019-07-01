from django.db import models
from indicator.models import Currency


class Uf(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


    def __str__(self):

    	return '<%s: %s>' % (self.date, self.value)

    class Meta:
        verbose_name_plural = 'uefes'
