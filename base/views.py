from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages

from .forms import RegistrationForm, UpdateProfileForm, LoginForm

""" - MOSTRAR OS ERROS NA PÁGINA
{% if form.errors %}
  <div class="alert alert-danger">
    <strong>Error:</strong> {{ form.errors }}
  </div>
{% endif %}
"""
# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        username = form.username
        email = form.email
        pass1 = form.pass1
        pass2 = form.pass2
        
        if User.objects.filter(username=username):
            messages.error(request, "Username já existe!")
            return redirect('register')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email já existe!")
            return redirect('register')
            
        if len(username) > 12:
            messages.error(request, "Username deve conter menos que 12 caracteres!")
            return redirect("register")
        
        if pass2 != pass1:
            messages.error(request, "Passwords não coincidem!")
            return redirect("register")
        
        if not form.username.isalnum:
            messages.error(request, "Passwords não coincidem!")
            return redirect("register")
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = form.fname
        myuser.last_name = form.lname
        
        myuser.save()
    
        messages.success(request, "Conta criada com sucesso!")
        return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'base/register.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado!")
            return redirect('profile')  # Redirect to the profile page or another appropriate page
        else:
            messages.error(request, "Perfil não foi atualizado. Verifica os campos!")
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'base/update_profile.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            # Log the user in
            messages.success(request, "Login com sucesso!")
            return redirect('home')  # Redirect to the desired page after login
        else:
            messages.error(request, "Username ou Password incorretos!")
    else:
        form = LoginForm()

    return render(request, 'base/login.html', {'form': form})