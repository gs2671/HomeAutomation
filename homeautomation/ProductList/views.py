from django.shortcuts import render
from django.http import Http404

from ProductList.models import Item

# Create your views here.
def index(request):
    items=Item.objects.exclude(price=0.0)
    return render(request,'ProductList/index.html',{
        'items':items,      
        })

    #return HttpResponse('<p>In index view</p>')

def item_detail(request,id):
    try:
        item=Item.objects.get(id=id)
        #return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))
    except Item.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request,'ProductList/item_detail.html',{
        'item':item
        })




