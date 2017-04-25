# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-25 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductList', '0018_merge_20170425_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='user',
            name='devices',
            field=models.TextField(choices=[('AmazonEcho', 'AmazonEcho'), ('Google Home', 'Google Home'), ('Ring Video Doorbell', 'Ring Video Doorbell'), ('Logitech Harmony Home Hub', 'Logitech Harmony Home Hub'), ('Nest Thermostat', 'Nest Thermostat'), ('Ecobee Remote Sensor', 'Ecobee Remote Sensor'), ('Philips Hue', 'Philips Hue'), ('Bose sound link Bluetooth Speaker', 'Bose sound link Bluetooth Speaker')], default='None'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
