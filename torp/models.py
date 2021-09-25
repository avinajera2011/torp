from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


class InventoryData(models.Model):
    id_name = models.CharField(max_length=200)
    demand = models.FloatField()                                                                 # a
    production_rate = models.FloatField()                                                        # r
    setup_order_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')       # k
    inventory_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')         # h
    unit_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')              # c
    shortage_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')          # u

    def __str__(self):
        return self.id_name
