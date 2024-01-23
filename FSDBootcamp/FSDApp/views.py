from django.shortcuts import render,redirect
from django.http import HttpResponse
from FSDApp.models import registeredUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from .forms import RegisterForm, LoginForm
User = get_user_model()

# Create your views here.
def base(request):
    return render(request,'FSDApp/base.html')

# def register(request):
#     if request.method == 'POST':
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#         contact=request.POST['contact']
#         email=request.POST['email']
#         pass1=request.POST['pass1']
#         pass2=request.POST['pass2']
#         print(fname,lname,contact,email,pass1,pass2)
#         if pass1 != pass2:
#             return HttpResponse("Sorry Passwords Doesnt match")
#         else:
#             ins= registeredUser(first_name=fname,last_name=lname, contact=contact)
#             ins.save()
#             my_user=User.objects.create_user(email,pass1)
#             my_user.save()
#             print(f"First Time User {fname}  {lname} and {email} has been created sucessfully")
#             return redirect('home')
#     return render(request, 'FSDApp/register.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            contact = form.cleaned_data['your_contact']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return render(request, 'FSDApp/invalid_passwords.html')
            
            # Save the user data to your User model or registeredUser model
            # Assuming you have a registeredUser model with email and password fields
            ins = registeredUser(first_name=fname, last_name=lname, contact=contact)
            ins.save()

            # Create a User model instance (Django's built-in authentication model)
            my_user = User.objects.create_user(email, password1)
            my_user.save()

            print(f"First Time User {fname} {lname} with email {email} has been created successfully")
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'FSDApp/register.html', {'form': form})

# def login(request):
#     if request.method=='POST':
#         user=authenticate(request,
#                           email=request.POST['email'],
#                           password=request.POST['pass1']
#                           )
#         print(user)
#         if user is not None:
#             auth_login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse("Invalid Credentials")
#     return render(request, 'FSDApp/login.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                return render(request, 'FSDApp/invalid_credentials.html')
    else:
        form = LoginForm()

    return render(request, 'FSDApp/login.html', {'form': form})

def home(request):
    return render(request, 'FSDApp/home.html')