from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

# Create your models here.
from product.models import Product


class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True, verbose_name=_('Birth Date'))
    # to log with email
    # email overwrite to be unique
    # removed from required fields list
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @property
    def last_order_date(self):
        return self.orders.order_by('-date').first().date

    @property
    def first_order_date(self):
        return self.orders.order_by('date').first().date

    @property
    def average_order_value(self):
        return self.orders.aggregate(Sum('total'))['total__sum']


class WishList(models.Model):
    customer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Customer'),
        related_name='wishlist'
    )
    products = models.ManyToManyField(
        Product,
        related_name='wishlists'
    )
