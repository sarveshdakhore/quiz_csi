from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, '../templates/home/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    redirect_to = request.GET.get('next', 'home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(redirect_to)
            
        else:
            return render(request, '../templates/home/login.html', {'form': form, 'next': redirect_to})
    else:
        form = AuthenticationForm()
        return render(request, '../templates/home/login.html', {'form': form, 'next': redirect_to})

def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, '../templates/home/signup.html', {'form': form})