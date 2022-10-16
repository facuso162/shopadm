from dataclasses import fields
from django.forms import ModelForm
from .models import Producto

class ProductCreationForm(ModelForm):

    class Meta:
        model = Producto
        exclude = ['usuario']