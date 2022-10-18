from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm, ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "placeholder"
            ] = "Nombre de Usuario"
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "class"
            ] = "form-control"
            self.fields[self._meta.model.USERNAME_FIELD].help_text = ""

    error_messages = {
        "password_mismatch": "Las contraseñas no coinciden",
    }

    password1 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Contraseña",
            "class": "form-control",
            }),
        error_messages={
            "required": "Este campo debe ser rellenado",
        },
        help_text=""
    )

    password2 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Repita la contraseña",
            "class": "form-control",
            }),
        error_messages={
            "required": "Este campo debe ser rellenado",
        }
    )

    class Meta():
        model = User
        fields = [
            "username",
        ]
        labels = {
            "username":"",
        }
        widgets = {
            "placeholder": "Nombre de usuario",
        }
