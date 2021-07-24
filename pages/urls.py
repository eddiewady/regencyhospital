from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [  
    path('',views.index,name='index'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('view_patient', views.view_patient, name='view_patient'),
    path('view_appointment', views.view_appointment, name='view_appointment'),
    path('view_doctor', views.view_doctor, name='view_doctor'),
    path('emergency_patient', views.emergency_patient, name='emergency_patient'),
    path('view_rooms', views.view_rooms, name='view_rooms'), 
    path('add_doctor', views.add_doctor, name='add_doctor'), 
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup')
]




