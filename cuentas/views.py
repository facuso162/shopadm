from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistroForm

# Create your views here.

@login_required(login_url='login')
def homeView(request):
    context = {'opcion': 0}
    return render(request, 'home.html', context)

def registroView(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegistroForm()

        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')

        context = {'form': form}

        return render(request, 'cuentas/registro.html', context)

def loginView(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request=request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')

        return render(request, 'cuentas/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')