from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    razonsocial=forms.CharField(max_length=50)
    email=forms.EmailField()

class PedidoForm(forms.Form):
    sabor=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()
    cliente = forms.ModelChoiceField(queryset=User.objects.all()) #BORRAR MAYYYYBE

class FacturaForm(forms.Form):
    cliente=forms.ModelChoiceField(queryset=User.objects.all())
    sabor=forms.CharField(max_length=50)
    precio=forms.IntegerField()
    peso=forms.IntegerField()
    #subtotal=forms.IntegerField()
    #fecha=forms.DateField()

class SaboresForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    precio=forms.IntegerField()


class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Mail usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class MensajeForm(forms.Form):
    receptor=forms.ModelChoiceField(queryset=User.objects.all())
    texto=forms.CharField(max_length=500)
    
    class Meta:
        model=User
        fields=["receptor", "texto"]
        help_texts = {k:"" for k in fields}


############ AVATAR
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")



