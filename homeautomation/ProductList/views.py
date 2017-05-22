from django.shortcuts import render,redirect
from __builtin__ import True
from django.http import HttpResponse,Http404,HttpResponseRedirect
#from django.contrib.auth import(
#    authenticate,
#    get_user_model,
#    login,
#    logout,
#)
from .forms import CustomUserLoginForm,CustomUserRegistrationForm, CommentForm
from ProductList.models import *
from uuid import UUID
import sys
from amazon.api import AmazonAPI
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.

def index(request):    
    if 'user_id' in request.session:
        #Getting User object
        user=CustomUser.objects.get(id=UUID(request.session['user_id']));
        cart_items={};

        #Getting Category start filter value
        if('category' in request.GET):
            categoryVal = request.GET.get('category')
        else:
            categoryVal="None";

        #Getting catgory bundles
        if(categoryVal=="None"):
            bundles=Bundle.objects.exclude(price=0.0)
        else:
            bundles=Bundle.objects.filter(category=categoryVal).exclude(price=0.0)

        #Subtracting user items from bundle price
        #rpdb2.start_embedded_debugger("guru")
        test=""
        for bundle in bundles:
            bundle.id=str(bundle.id)
            for bundleItem in bundle.items.all():
                bundle.items_custom.append(bundleItem)
                if bundleItem in user.items.all():
                    bundleItem.isOwned=True                     
                    bundle.price=bundle.price-bundleItem.price
                    bundle.userOwned+=1
                else:
                    if(cart_items.has_key(str(bundle.id))):
                        cart_items[str(bundle.id)].append(str(bundleItem.asin))
                    else:
                        cart_items[str(bundle.id)]=[str(bundleItem.asin)]

        #    test+=str(hex(id(bundle.items_custom)))+"------"

        #return HttpResponse('<p>'+test+'</p>')

        #Getting Budget start filter value
        if('budget' in request.GET):
            budgetVal=request.GET.get('budget')
            if(budgetVal=="None"):
                budgetStart=0
                budgetEnd=sys.maxint
            else:
                budgetStart,budgetEnd = budgetVal.split(',',1)
                budgetStart=int(budgetStart)
                budgetEnd=int(budgetEnd)
        else:
            budgetVal="None";
            budgetStart=0;
            budgetEnd=sys.maxint;

        #Applying Budget filter to bundles
        filteredBundles=[]
        for bundle in bundles:
            if(bundle.price>budgetStart and bundle.price<=budgetEnd):
                filteredBundles.append(bundle)
        #bundles=bundles.filter(price__gt=budgetStart,price__lte=budgetEnd).exclude(price=0.0)      


        return render(request,'ProductList/index.html',{
            'bundles':filteredBundles,
            'category':categoryVal,
            'budget':budgetVal,
            'user':user,
            'cart_items':cart_items,
            })
    else:
        return redirect('/login/')

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

def login_view(request):
    #print(request.user.is_authenticated())
    title="login"
    form=CustomUserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        #user=authenticate(username=username, password=password)
        user=CustomUser.objects.get(username=username)
        if(str(user.username)==username and str(user.password)==password):
            request.session['user_id'] = str(user.id)
            return redirect('/')
            #return render(request, "ProductList/index.html",{"user":user})
        #login(request, user)
        #print(request.user.is_authenticated())
        #return redirect('/')
    return render(request, "form.html",{"form":form, 'title':title})

def register_view(request):
    print(request.user.is_authenticated())
    title="Register"
    form=CustomUserRegistrationForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password = form.cleaned_data.get('password')
        #user.set_password(password)
        user=CustomUser(username=user.username, password=password, email=user.email, devices=user.devices)
        user.save()
        #new_user=authenticate(username=user, password=password)
        #login(request, new_user)
        return redirect('/login/')
    context = {
    "form":form,
    "title":title
    }

    return render(request, "form.html",context)

def logout_view(request):
    #logout(request)
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, "form.html",{})

def user_profile(request,username):
    user=CustomUser.objects.get(id=UUID(request.session['user_id']));
    return render(request, "ProductList/profile.html",{'user':user})

def add_to_cart(request,cartItems):
    amazon = AmazonAPI('Access Key', 'Secret Key', 'gs2671-20')
    flag=True
    cartItems=eval(cartItems)
    for item in cartItems:       
        if(flag):
            product = amazon.lookup(ItemId=item)  
            amazon_cart = amazon.cart_create([{'offer_id':product.offer_id,'quantity': 1}])
            flag=False
        else:
            product = amazon.lookup(ItemId=item)
            amazon.cart_add({'offer_id':product.offer_id,'quantity': 1}, amazon_cart.cart_id, amazon_cart.hmac)
    return HttpResponseRedirect(amazon_cart.purchase_url)    



