from django.urls import path

from .views import productosListView, agregarProductoView


urlpatterns = [
    path('productos', productosListView, name='productos'),
    path('agregarProducto', agregarProductoView, name='agregarProducto'),
]