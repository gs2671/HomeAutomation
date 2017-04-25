from django.contrib import admin

# Register your models here.
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display=['title','price']


admin.site.register(Bundle)
admin.site.register(Item,ItemAdmin)
admin.site.register(Comment)


#class BundleAdminForm(ModelForm):
#    class Meta:
#        model=Bundle
#        fields = '__all__'

#    def clean(self):
#        price=20.0
#        items=list(self.cleaned_data['items'])
#        for item in items:
#            price=price+item.price
#        self.cleaned_data['price']=price
#        return self.cleaned_data

#class BundleAdmin(admin.ModelAdmin):
#    model=Bundle
#    form=BundleAdminForm