from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def inicioAppClientes(request):
    return render(request, "AppClientes/index.html")

def pedidos(request):
    return render(request, "AppClientes/pedidos.html")

def facturas(request):
    return render(request, "AppClientes/facturas.html")

def precios(request):
    return render(request, "AppClientes/precios.html")

def inbox(request):
    return render(request, "AppClientes/inbox.html")

def nuevomensaje(request):
    return render(request, "AppClientes/nuevomensaje.html")