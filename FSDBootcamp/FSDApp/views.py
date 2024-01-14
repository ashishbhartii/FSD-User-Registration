from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def land(request):
    return render(request,"FSDApp/land.html")

def registration(request):
    return render(request,"FSDApp/registration.html")

def login(request):
    return HttpResponse(request,"FSDApp/login.html")

def main(request):
    return HttpResponse(request,"FSDApp/main.html")
