# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-23 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductList', '0014_bundle_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='price',
            field=models.FloatField(default=0.0, editable=False),
        ),
    ]
