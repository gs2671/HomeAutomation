from django.shortcuts import render
from django.http import HttpResponse,Http404

from ProductList.models import *

# Create your views here.
def index(request,categoryname=None):
    if(categoryname is None):    
        items=Item.objects.exclude(price=0.0)
        return render(request,'ProductList/index.html',{
            'items':items,      
            })
    else:
        items=Item.objects.filter(category=categoryname)
        return render(request,'ProductList/index.html',{
            'items':items,      
            })

    #return HttpResponse('<p>In index view</p>')

def item_detail(request,id):
    try:
        item=Item.objects.get(id=id)
        if(item is not None):
            comments=Comment.objects.filter(item__id=id)
            #return HttpResponse('<p>No of commetns found {0}</p>'.format(len(comments)))
        #else:
            #return HttpResponse('<p>No Comments</p>')
    except Item.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request,'ProductList/item_detail.html',{
        'item':item,
        'comments':comments
        })




