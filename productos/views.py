from itertools import count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Producto
from .forms import ProductCreationForm
# Create your views here.

@login_required(login_url='login')
def productosListView(request):

    productos = Producto.objects.all()

    cantidad = productos.count()

    context = {
        'opcion':1,
        'productos':productos,
        'cantidad': cantidad,
        }

    return render(request, 'home.html', context)

@login_required(login_url='login')
def agregarProductoView(request):

    form = ProductCreationForm(usuario=request.user)

    if request.method == 'POST':
        form = ProductCreationForm(request.POST, usuario=request.user)
        if form.is_valid():
            form.save()
            return redirect('productos')

    context = {
        'opcion':2,
        'form':form,
        }

    return render(request, 'home.html', context)

    