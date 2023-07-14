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
            #login_form.add_error(None, 'Ingreso exitoso')
            return redirect('index')
        else:
            messages.warning(request, 'Credenciales inválidas')
            #login_form.add_error(None, 'Credenciales inválidas')
    data['form'] = login_form
    
    return render(request, template_name, data)
    
    """ if request.method == 'POST':
        form = MyLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            print(user)
            
            if user:
                login(request, user)
                return redirect('index')  # Redirige a la página de inicio después del inicio de sesión exitoso
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = MyLoginForm()
    
    return render(request, 'registration/login.html', {'form': form}) """

def mylogout(request):
    logout(request)
    return redirect('registration.login')

def index(request):
    return render(request, template_name='index.html')