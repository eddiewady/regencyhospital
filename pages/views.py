from django.shortcuts import render
from django.http  import HttpResponse


def index(request):
    return render(request,'pages/index.html')

def add_patient(request):
    return render(request,'pages/add_patient.html')

def view_patient(request):
    return render(request,'pages/view_patient.html')

def view_appointment(request):
    return render(request,'pages/view_appointment.html')

def view_doctor(request):
    return render(request,'pages/view_doctor.html')

def emergency_patient(request):
    return render(request,'pages/emergency_patient.html')

def view_rooms(request):
    return render(request,'pages/view_rooms.html')

def add_doctor(request):
    return render(request,'pages/add_doctor.html')
def login(request):
    return render(request,'pages/login.html')

def logout(request):
    return render(request,'pages/logout.html')

def signup(request):
    return render(request,'pages/signup.html')