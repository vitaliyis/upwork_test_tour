# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=128)),
                ('hotel', models.CharField(max_length=256)),
                ('start', models.DateField()),
                ('finish', models.DateField()),
                ('quantity_days', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
