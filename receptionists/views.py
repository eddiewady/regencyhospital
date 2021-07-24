from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'receptionists/receptionists.html')
 
def receptionist(request): 
    return render(request,'receptionists/receptionist.html')
