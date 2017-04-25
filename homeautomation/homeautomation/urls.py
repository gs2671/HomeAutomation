"""homeautomation_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include,url
from django.contrib import admin
from django.conf.urls.static import static
from ProductList.views import (login_view, register_view, logout_view)

from ProductList import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^category/(?P<categoryname>.*)/',views.index,name="filtered_index"),
    url(r'^item/(?P<id>\d+)/',views.item_detail,name='item_detail'),
    url(r'^ProductList/',include('ProductList.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/',register_view,name="register"),
    url(r'^login/',login_view,name="login"),
    url(r'^logout/',logout_view,name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
