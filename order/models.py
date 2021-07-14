from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
from rest_framework.exceptions import ValidationError

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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.total = self.product.price * self.quantity

        if self.product.inventory < self.quantity:
            raise ValidationError({
                'product': "Out Of Stock"
            })
        if self.total <= 10000:
            self.product.inventory = self.product.inventory - self.request.data['quantity']
            self.product.save()
            super(Order, self).save(force_insert, force_update, using, update_fields)
        else:
            raise ValidationError({
                'total_of_order': "bigger than 10000.0"
            })
