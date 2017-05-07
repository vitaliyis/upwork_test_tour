# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Оплачено'),
        ),
    ]
