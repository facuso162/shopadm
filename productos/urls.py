from django.urls import path

from .views import productosListView, agregarProductoView, editarProductoView, eliminarProductoView


urlpatterns = [
    path('productos', productosListView, name='productos'),
    path('agregarProducto', agregarProductoView, name='agregarProducto'),
    path('editarProducto/<str:pk>', editarProductoView, name='editarProducto'),
    path('eliminarProducto/<str:pk>', eliminarProductoView, name='eliminarProducto'),
]