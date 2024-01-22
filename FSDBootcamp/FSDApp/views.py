from django.shortcuts import render,redirect
from django.http import HttpResponse
from FSDApp.models import registeredUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def base(request):
    return render(request,'FSDApp/base.html')

def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        print(fname,lname,contact,email,pass1,pass2)
        if pass1 != pass2:
            return HttpResponse("Sorry Passwords Doesnt match")
        else:
            ins= registeredUser(first_name=fname,last_name=lname, contact=contact)
            ins.save()
            my_user=User.objects.create_user(email,pass1)
            my_user.save()
            print(f"First Time User {fname}  {lname} and {email} has been created sucessfully")
            return redirect('home')
    return render(request, 'FSDApp/register.html')

def login(request):
    if request.method=='POST':
        user=authenticate(request,
                          email=request.POST['email'],
                          password=request.POST['pass1']
                          )
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, 'FSDApp/login.html')

def home(request):
    return render(request, 'FSDApp/home.html')