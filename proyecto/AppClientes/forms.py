from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
    razonsocial=forms.CharField(max_length=50)
    sabor=forms.CharField(max_length=50)
    precio=forms.IntegerField()
    peso=forms.FloatField()
    subtotal=forms.FloatField()
    fecha=forms.DateField()

class SaboresForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    precio=forms.IntegerField()


class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="mail usuario")
    password1=forms.CharField(label="constraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="repetir constraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

