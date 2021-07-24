from django import urls
from django.conf.urls import url
from django .urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.index,name='receptionists'),
    path('receptionist',views.receptionist,name='receptionist'),

 
    
]