import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.IntegerField(blank=True, default=0)
    imagen = models.ImageField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')