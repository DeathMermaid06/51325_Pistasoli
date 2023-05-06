from django.db import models
from django.contrib.auth.models import User
import datetime


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
    cliente = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    precio = models.IntegerField()
    peso = models.IntegerField()
    fecha = models.DateField(default=datetime.date.today)

    @property
    def subtotal(self):
        return self.precio * self.peso

    def __str__(self):
        return f"{self.cliente} ${self.subtotal} {self.fecha}"
    
    
class Sabores(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} ${self.precio}"
    

class Mensaje(models.Model):
    emisor=models.ForeignKey(User, on_delete=models.CASCADE)
    receptor=models.CharField(max_length=50)
    texto=models.CharField(max_length=500)
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.fecha} - {self.texto} - {self.receptor} - {self.emisor}"
    
class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)