from dataclasses import fields
from django.forms import ModelForm
from .models import Producto

class ProductCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super(ProductCreationForm, self).__init__(*args, **kwargs)

    def super(self, *args, **kwargs):
        self.instance.usuario = self.usuario
        super(ProductCreationForm, self).save(*args, **kwargs)

    class Meta:
        model = Producto
        #exclude = ['usuario']
        fields = '__all__'