# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-23 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductList', '0011_auto_20170422_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='_price',
            field=models.FloatField(default=0.0),
        ),
    ]
