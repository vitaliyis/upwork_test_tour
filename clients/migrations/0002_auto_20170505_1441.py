# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='middle_name',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='clients',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone1',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone2',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]