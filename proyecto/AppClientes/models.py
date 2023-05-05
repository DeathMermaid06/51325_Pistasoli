from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    razonsocial=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Authentication

class Pedido(models.Model):
    sabor=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.sabor} - {self.cantidad}"

class Factura(models.Model):
    razonsocial=models.CharField(max_length=50)
    sabor=models.CharField(max_length=50)
    precio=models.IntegerField()
    peso=models.FloatField()
    subtotal=models.FloatField()
    fecha=models.DateField()
    def __str__(self):
        return f"{self.razonsocial} ${self.subtotal} {self.fecha}"
    
class Sabores(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} ${self.precio}"