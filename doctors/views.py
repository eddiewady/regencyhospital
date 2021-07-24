from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'doctors/doctors.html')
 
def doctor(request): 
    return render(request,'doctors/doctor.html')

def search(request):
    return render(request,'doctors/search.html')

