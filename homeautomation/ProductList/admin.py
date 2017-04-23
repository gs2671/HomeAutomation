from django.contrib import admin

# Register your models here.
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display=['title','price']



admin.site.register(Item,ItemAdmin)
admin.site.register(Comment)
admin.site.register(User)
