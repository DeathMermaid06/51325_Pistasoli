from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
            form = SaboresForm() 
    else:
       form = SaboresForm() 

    sabores = Sabores.objects.all()
    context= {"sabores": sabores, "form": form}
    return render(request, ("AppClientes/precios.html"), context)

#HttpResponseRedirect TENGO QUE USARLO PORQUE ME QUEDA EL ID DEL POST ANTERIOR Y FALLA SI NO LO ENCUENTRA O SOBREESCRIBE EL ID ANTERIOR 

def preciosborrar(request, id):
    sabor=Sabores.objects.get(id=id)
    sabor.delete()
    sabores = Sabores.objects.all()
    form = SaboresForm()
    return HttpResponseRedirect(reverse('precios'), {"sabores": sabores, "mensaje": "SABOR ELIMINADO CORRECTAMENTE", "form": form})
    
def precioseditar(request, id):
    sabor=Sabores.objects.get(id=id)
    if request.method == "POST":
        form = SaboresForm(request.POST)
        if form.is_valid():
            sabor = Sabores.objects.get(id=id)
            sabor.nombre = form.cleaned_data["nombre"]
            sabor.precio = form.cleaned_data["precio"]
            sabor.save()
            form = SaboresForm() 
            sabores = Sabores.objects.all()
            return HttpResponseRedirect(reverse('precios'), {"sabores": sabores, "mensaje": "SABOR EDITADO CORRECTAMENTE", "form": form})
        else:
            form = SaboresForm() 
    else:
       form = SaboresForm(initial={"nombre": sabor.nombre, "precio": sabor.precio})

       return render(request, ("AppClientes/precioseditar.html"), {"form": form})



def inbox(request):
    return render(request, "AppClientes/inbox.html")

def nuevomensaje(request):
    return render(request, "AppClientes/nuevomensaje.html")

def loginregisterC(request):
    return render(request, "AppClientes/login.html")

def registerC(request):
    return render(request, "AppClientes/register.html")