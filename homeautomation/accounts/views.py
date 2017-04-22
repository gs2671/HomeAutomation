# -*- coding: utf-8 -*-
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegistrationForm
# Create your views here.
def login_view(request):
    print(request.user.is_authenticated())
    title="login"
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('/')
    return render(request, "form.html",{"form":form, 'title':title})

def register_view(request):
    print(request.user.is_authenticated())
    title="Register"
    form=UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=username, password=password)
        login(request, new_user)
    context = {
    "form":form,
    "title":title
    }
    return redirect('/')
    return render(request, "form.html",context)


def logout_view(request):
    logout(request)
    return render(request, "form.html",{})
