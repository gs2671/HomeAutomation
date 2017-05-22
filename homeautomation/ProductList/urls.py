from django.conf.urls import url
from django.utils.functional import curry
from django.views.defaults import *
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    ]

handler500 = curry(server_error, template_name='500.html')
handler404 = curry(page_not_found, template_name='404.html')
handler403 = curry(permission_denied, template_name='403.html')