# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-23 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductList', '0015_auto_20170422_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]