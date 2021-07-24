
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('',include('pages.urls')),
    path('doctors/',include('doctors.urls')),
     path('receptionists/',include('receptionists.urls')),
    path('admin/', admin.site.urls),
]
