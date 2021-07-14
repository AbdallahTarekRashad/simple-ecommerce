from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
from account.models import User
from product.models import Product


class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='orders'
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name=_('Customer'),
        related_name="orders",
        null=True
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name=_('Quantity')
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date')
    )

    total = models.FloatField(
        validators=[MaxValueValidator(1000.0)],
    )
