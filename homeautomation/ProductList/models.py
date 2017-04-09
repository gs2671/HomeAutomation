from __future__ import unicode_literals
import datetime

from django.db import models

# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.FloatField(default=0.0)

class Comment(models.Model):
    text=models.TextField()
    createdon=models.DateTimeField(default=datetime.datetime.now)    
    item=models.ForeignKey(Item)