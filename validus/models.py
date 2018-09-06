from django.db import models
from django.contrib import admin

import validus.settings as settings

class Currency(models.Model):
    CURRENCY_CHOICES = (
        ('GBPUSD', 'GBPUSD'),
        ('GBPEUR', 'GBPEUR'),
    )
    valuation_date = models.DateField()
    underlying = models.CharField(
        max_length=6,
        choices=CURRENCY_CHOICES,
        default='GBPEUR'
    )
    mid = models.FloatField()


admin.site.register(Currency)