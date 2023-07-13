from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import MyLoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

# Create your views here.

# Login personalizado

def mylogin(request):
    template_name ='registration/login.html'
    data = { 'form': MyLoginForm() }
    login_form = MyLoginForm()
    
    if request.method == 'POST':
        login_form = MyLoginForm(data = request.POST)
        
        if login_form.is_valid():
            user = authenticate(username = login_form.cleaned_data['username'], password = login_form.cleaned_data['password'])
            login(request, user)
            messages.success(request, '¡Ingreso exitoso!')
            return redirect('index')
        else:
            for field, errors in login_form.errors.items():
                for error in errors:
                    messages.error(request, 'Error en los datos, por favor verifique que sean los correctos')
    data['form'] = login_form
    
    return render(request, template_name, data)

def mylogout(request):
    logout(request)
    return redirect('registration.login')

def index(request):
    return render(request, template_name='index.html')