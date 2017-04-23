from __future__ import unicode_literals
import datetime

from django.db import models
from django.forms import ModelForm, modelformset_factory
from django.core.urlresolvers import reverse


# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=200)
    image=models.FileField(null=True, blank=True)
    description=models.TextField()
    category=models.TextField(choices=[("Kitchen","Kitchen"),("Entertainment","Entertainment"),("Bedroom","Bedroom"),("None","None")], default="None")
    price=models.FloatField(default=0.0)

class Comment(models.Model):
    text=models.TextField()
    createdon=models.DateTimeField(default=datetime.datetime.now)
    item=models.ForeignKey(Item)

class User(models.Model):
    username= models.TextField(max_length=200,default='None')    
    password= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    # First option is data value sshould be changed to item code later
    OPTIONS = [
            ("Amazon Echo", "Amazon Echo"),
            ("Google Home", "Google Home"),
            ("Ring Video Doorbell","Ring Video Doorbell"),
            ('Logitech Harmony Home Hub','Logitech Harmony Home Hub'),
            ('Nest Thermostat','Nest Thermostat'),
            ('Ecobee Remote Sensor','Ecobee Remote Sensor'),
            ('Philips Hue','Philips Hue'),
            ('Bose sound link Bluetooth Speaker','Bose sound link Bluetooth Speaker')
            ]
    devices = models.TextField(choices=OPTIONS,default='None')

# class CommentForm(ModelForm):
#     class Meta:
#         model=Comment
#         fields=['text','createdon','item']
# def get_absolute_url(self):
#     return reverse("items:detail",kwargs={"id":self.id})
