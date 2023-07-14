from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.index), name = 'index'),
    path('login', views.mylogin, name = 'registration.login'),
    path('logout', views.mylogout, name='registration.logout'),
    
    path('add', login_required(views.add_app), name = 'add_app')
]