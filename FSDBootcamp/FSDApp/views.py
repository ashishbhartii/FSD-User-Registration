from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request,"FSDApp/landingPage.html")

def registration(request):
    return render(request,"FSDApp/registration.html")

def login(request):
    return render(request,"FSDApp/login.html")

def main(request):
    return render(request,"FSDApp/main.html")
