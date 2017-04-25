from __future__ import unicode_literals
import datetime
import uuid

from django.db import models
from django.forms import ModelForm, modelformset_factory
from django.core.urlresolvers import reverse
from django.db.models.signals import m2m_changed
from django.dispatch import receiver



#Create your models here
class Item(models.Model):
    title=models.CharField(max_length=200)
    image=models.FileField(null=True, blank=True)
    description=models.TextField()
    category=models.TextField(choices=[("Kitchen","Kitchen"),("Entertainment","Entertainment"),("Bedroom","Bedroom"),("None","None")], default="None")
    price=models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    def __iter__(self):
        yield self   

class Comment(models.Model):
    text=models.TextField()
    createdon=models.DateTimeField(default=datetime.datetime.now)
    item=models.ForeignKey(Item)

class CustomUser(models.Model):
    username= models.CharField(max_length=200,default='None')    
    password= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    # First option is data value sshould be changed to item code later
    OPTIONS = [
            ("AmazonEcho", "AmazonEcho"),
            ("Google Home", "Google Home"),
            ("Ring Video Doorbell","Ring Video Doorbell"),
            ('Logitech Harmony Home Hub','Logitech Harmony Home Hub'),
            ('Nest Thermostat','Nest Thermostat'),
            ('Ecobee Remote Sensor','Ecobee Remote Sensor'),
            ('Philips Hue','Philips Hue'),
            ('Bose sound link Bluetooth Speaker','Bose sound link Bluetooth Speaker')
            ]
    #devices = models.TextField(choices=OPTIONS,default='None')
    devices = models.TextField(default='None')

class Bundle(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=200)
    category=models.TextField(choices=[("Kitchen","Kitchen"),("Entertainment","Entertainment"),("Bedroom","Bedroom"),("None","None")], default="None")
    description=models.TextField()
    items=models.ManyToManyField(Item)
    price=models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    def __iter__(self):
        yield self


@receiver(m2m_changed, sender=Bundle.items.through)
def recalculate_total(sender, instance, action, **kwargs):
    price=0.0
    for i in instance.items.all():
        price=price+i.price
        instance.price=price
        instance.save()
