# Generated by Django 3.1.5 on 2021-07-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]