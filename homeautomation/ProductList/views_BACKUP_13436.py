from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect

from .forms import CommentForm
from ProductList.models import *

# Create your views here.
<<<<<<< HEAD
def index(request,categoryname=None):
    if(categoryname is None):    
=======
def index(request,category=None):
    if(category is None):
>>>>>>> e659d8722fb4e2ed002907bf91c11b7477a613e9
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
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data['text']
                # form.save()
            item=Item.objects.get(id=id)
            if(item is not None):
                comments=Comment.objects.filter(item__id=id)
            comment=Comment(text=text,item=item)
            comment.save()
            return redirect(request.META['HTTP_REFERER'])
    try:
        item=Item.objects.get(id=id)
        if(item is not None):
            comments=Comment.objects.filter(item__id=id)
            #return HttpResponse('<p>No of commetns found {0}</p>'.format(len(comments)))
        #else:
            #return HttpResponse('<p>No Comments</p>')
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    form=CommentForm(request.POST)
    return render(request,'ProductList/item_detail.html',{
        'item':item,
        'comments':comments,
        'form':form
        })

def create_comment(request):
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=CommentForm()
    return  render(request, 'item_detail.html', {
        'form': form
    })
