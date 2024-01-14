from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.land, name='land'),
    path('registration',views.registration, name='registration'),
    path('login',views.login, name='login'),
    path('main',views.main, name='main'),
]