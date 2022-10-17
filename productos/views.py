from itertools import count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Producto
from .forms import ProductCreationForm
# Create your views here.

@login_required(login_url='login')
def productosListView(request):

    productos = Producto.objects.filter(usuario=request.user)

    cantidad = productos.count()

    context = {
        'opcion':1,
        'productos':productos,
        'cantidad': cantidad,
        }

    return render(request, 'home.html', context)

@login_required(login_url='login')
def agregarProductoView(request):

    form = ProductCreationForm()

    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            productoInstance = form.save(commit=False)
            productoInstance.usuario = request.user
            productoInstance.save()
            return redirect('productos')

    context = {
        'opcion':2,
        'form':form,
        }

    return render(request, 'home.html', context)

@login_required(login_url='login')
def editarProductoView(request, pk):

    p = Producto.objects.filter(id=pk)[0]
    
    form = ProductCreationForm(instance=p)

    if request.method == 'POST':
        form = ProductCreationForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('productos')

    context = {
        'opcion':2,
        'form':form,
    }

    return render(request, 'home.html', context)

@login_required(login_url='login')
def eliminarProductoView(request, pk):

    p = Producto.objects.filter(id=pk)[0]
    
    if request.method == 'POST':
        p.delete()
        return redirect('productos')

    context = {
        'opcion': 3,
        'producto': p,
    }

    return render(request, 'home.html', context)