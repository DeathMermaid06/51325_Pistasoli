from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from .forms import *

from .models import *

# Create your views here.
@login_required
def inicioAppClientes(request):
    return render(request, "AppClientes/index.html")

@login_required
def pedidos(request):
    return render(request, "AppClientes/pedidos.html")

@login_required
def facturas(request):
    return render(request, "AppClientes/facturas.html")

@login_required
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

@login_required
def preciosborrar(request, id):
    sabor=Sabores.objects.get(id=id)
    sabor.delete()
    sabores = Sabores.objects.all()
    form = SaboresForm()
    return HttpResponseRedirect(reverse('precios'), {"sabores": sabores, "mensaje": "SABOR ELIMINADO CORRECTAMENTE", "form": form})
    
@login_required    
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


@login_required
def inbox(request):
    return render(request, "AppClientes/inbox.html")

@login_required
def nuevomensaje(request):
    return render(request, "AppClientes/nuevomensaje.html")


def registerC(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppClientes/register_correcto.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppClientes/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppClientes/register.html", {"form": form})


def loginregisterC(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave) 
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppClientes/index.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppClientes/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppClientes/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppClientes/login.html", {"form": form})
    

    
    
    

