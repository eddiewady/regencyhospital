from django import urls
from django.conf.urls import url
from django .urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.index,name='doctors'),
     path('doctor',views.doctor,name='doctor'),
    path('search',views.search,name='search'),
 
    
]