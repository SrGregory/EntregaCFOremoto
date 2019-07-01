import uuid
from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'currencies'
