# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20170505_1450'),
        ('tours', '0002_auto_20170505_1450'),
        ('orders', '0002_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.Tour')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
    ]