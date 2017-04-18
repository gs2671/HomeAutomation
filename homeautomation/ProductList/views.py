from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect

from .forms import CommentForm
from ProductList.models import *
import sys

# Create your views here.
def index(request):
    #Getting Category filter value
    if('category' in request.GET):
        categoryVal = request.GET.get('category')
    else:
        categoryVal="None";

    #Getting Budget start filter value
    if('budget' in request.GET):
        budgetVal=request.GET.get('budget');
        if(budgetVal=="None"):
            budgetStart=0; 
            budgetEnd=sys.maxint;
        else:
            budgetStart,budgetEnd = budgetVal.split(',',1);
    else:
        budgetVal="None";
        budgetStart=0; 
        budgetEnd=sys.maxint;       
        

    if(categoryVal=="None" and budgetVal=="None"):    
        items=Item.objects.filter(price__gt=budgetStart,price__lte=budgetEnd).exclude(price=0.0)       
    elif(categoryVal!="None" and budgetVal!="None"):
        items=Item.objects.filter(price__gt=budgetStart,price__lte=budgetEnd,category=categoryVal).exclude(price=0.0) 
    elif(categoryVal=="None" and budgetVal!="None"):
        items=Item.objects.filter(price__gt=budgetStart,price__lte=budgetEnd).exclude(price=0.0) 
    else:
        items=Item.objects.filter(category=categoryVal).exclude(price=0.0) 
        
    return render(request,'ProductList/index.html',{
        'items':items,
        'category':categoryVal,
        'budget':budgetVal,
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
