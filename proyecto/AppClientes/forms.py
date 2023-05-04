from django import forms

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    razonsocial=forms.CharField(max_length=50)
    email=forms.EmailField()

class PedidoForm(forms.Form):
    sabor=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()

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