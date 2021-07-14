# Generated by Django 3.1.5 on 2021-07-14 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(1000.0)]),
        ),
    ]
