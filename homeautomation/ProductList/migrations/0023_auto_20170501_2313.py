# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductList', '0022_auto_20170501_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='devices',
        ),
        migrations.AddField(
            model_name='customuser',
            name='items',
            field=models.ManyToManyField(to='ProductList.Item'),
        ),
    ]
