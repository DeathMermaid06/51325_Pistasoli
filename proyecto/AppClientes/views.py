from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

from .models import *

# Create your views here.
def inicioAppClientes(request):
    return render(request, "AppClientes/index.html")

def pedidos(request):
    return render(request, "AppClientes/pedidos.html")

def facturas(request):
    return render(request, "AppClientes/facturas.html")

def precios(request):
    if request.method == "POST":
        form = SaboresForm(request.POST)
        if form.is_valid():
            sabor = Sabores()
            sabor.nombre = form.cleaned_data["nombre"]
            sabor.precio = form.cleaned_data["precio"]
            sabor.save()
    else:
       form = SaboresForm() 

    sabores = Sabores.objects.all()
    context= {"sabores": sabores, "form": form}
    return render(request, ("AppClientes/precios.html"), context)


def inbox(request):
    return render(request, "AppClientes/inbox.html")

def nuevomensaje(request):
    return render(request, "AppClientes/nuevomensaje.html")