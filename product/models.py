from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name=_('Name')
    )
    price = models.PositiveIntegerField(
        verbose_name=_('Price')
    )
    inventory = models.PositiveIntegerField(
        verbose_name=_('Inventory')
    )

    @property
    def out_of_stock(self):
        if self.inventory == 0:
            return True
        return False
