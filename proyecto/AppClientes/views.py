from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .forms import *

from .models import *
from AppMain.models import *

# Create your views here.


def verAvatar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/favicon.ico"
  

@login_required
def inicioAppClientes(request):
    return render(request, "AppClientes/index.html", {"avatar":verAvatar(request)})


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
    context= {"sabores": sabores, "form": form, "avatar":verAvatar(request)}
    return render(request, ("AppClientes/precios.html"), context)

#HttpResponseRedirect TENGO QUE USARLO PORQUE ME QUEDA EL ID DEL POST ANTERIOR Y FALLA SI NO LO ENCUENTRA O SOBREESCRIBE EL ID ANTERIOR (creeeeeo que podria haber usado reverselazy)

@login_required
def preciosborrar(request, id):
    sabor=Sabores.objects.get(id=id)
    sabor.delete()
    sabores = Sabores.objects.all()
    form = SaboresForm()
    return HttpResponseRedirect(reverse('precios'), {"sabores": sabores, "mensaje": "SABOR ELIMINADO CORRECTAMENTE", "form": form, "avatar":verAvatar(request)})
    
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
            return HttpResponseRedirect(reverse('precios'), {"sabores": sabores, "mensaje": "SABOR EDITADO CORRECTAMENTE", "form": form, "avatar":verAvatar(request)})
        else:
            form = SaboresForm() 
    else:
       form = SaboresForm(initial={"nombre": sabor.nombre, "precio": sabor.precio})

       return render(request, ("AppClientes/precioseditar.html"), {"form": form, "avatar":verAvatar(request)})



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
                return render(request, "AppClientes/index.html", {"mensaje":f"Usuario {usu} logueado correctamente", "avatar":verAvatar(request)})
            else:
                return render(request, "AppClientes/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppClientes/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppClientes/login.html", {"form": form})


#me fijo si es superuser y muestro todo. Sino solo muestro los resultados del cliente en particular
@login_required
def vista_super (request):
    if request.user.is_superuser:
        pedidos = Pedido.objects.all()
        context= {"pedidos": pedidos, "avatar":verAvatar(request)}
        return render(request, "AppClientes/pedidos.html", context)
    else:
        #return redirect("pedidos_por_cliente")
        varCliente = request.user
        pedidos = Pedido.objects.filter(cliente=varCliente)
        context= {"pedidos": pedidos, "avatar":verAvatar(request)}
        return render(request, "AppClientes/pedidos_por_cliente.html", context)


#class PedidoPorUsuario(LoginRequiredMixin, ListView):
#    model = Pedido
#    template_name ='AppClientes/pedido_por_usuario.html'
    
#    def get_queryset(self):
#        return Pedido.objects.filter(cliente=self.request.user)
    
    
    
#CRUD de pedidos

@login_required
def pedidoAgregar(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = Pedido()
            pedido.sabor = form.cleaned_data["sabor"]
            pedido.cantidad = form.cleaned_data["cantidad"]
            pedido.cliente = form.cleaned_data["cliente"] ## Borrar maybe si lo saco de la form
            pedido.save()
            form = PedidoForm() 
            context={"avatar":verAvatar(request)}
            return HttpResponseRedirect(reverse('pedidosagregar'), context)
    else:
       form = PedidoForm() 

    pedidos = Pedido.objects.all()
    context= {"pedidos": pedidos, "form": form, "avatar":verAvatar(request)}
    return render(request, ("AppClientes/pedidosagregar.html"), context)


@login_required
def pedidosborrar(request, id):
    pedidos=Pedido.objects.get(id=id)
    pedidos.delete()
    pedidos = Pedido.objects.all()
    form = PedidoForm()
    return HttpResponseRedirect(reverse('pedidos_por_cliente'), {"pedidos": pedidos, "mensaje": "PEDIDO ELIMINADO CORRECTAMENTE", "form": form, "avatar":verAvatar(request)})

@login_required
def pedidosborrarS(request, id):
    pedidos=Pedido.objects.get(id=id)
    pedidos.delete()
    pedidos = Pedido.objects.all()
    form = PedidoForm()
    return HttpResponseRedirect(reverse('pedidos_super'), {"pedidos": pedidos, "mensaje": "PEDIDO ELIMINADO CORRECTAMENTE", "form": form, "avatar":verAvatar(request)})
    
## FACTURA

@login_required
def vista_superFactura (request):
    if request.user.is_superuser:
        facturas = Factura.objects.all()
        context= {"facturas": facturas, "avatar":verAvatar(request)}
        return render(request, "AppClientes/facturas.html", context)
    else:
        varCliente = request.user
        facturas = Factura.objects.filter(cliente=varCliente)
        context= {"facturas": facturas, "avatar":verAvatar(request)}
        return render(request, "AppClientes/facturas_por_cliente.html", context)
    

@login_required
def facturaAgregar(request):
    if request.method == "POST":
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = Factura()
            factura.cliente = form.cleaned_data["cliente"]
            factura.sabor = form.cleaned_data["sabor"]
            factura.peso = form.cleaned_data["peso"] 
            factura.precio = form.cleaned_data["precio"] 
            factura.save()
            form = FacturaForm() 
            context={"avatar":verAvatar(request)}
            return HttpResponseRedirect(reverse('facturasagregar'), context)
    else:
       form = FacturaForm() 

    facturas = Factura.objects.all()
    context= {"facturas": facturas, "form": form, "avatar":verAvatar(request)}
    return render(request, ("AppClientes/facturasagregar.html"), context)


#### PERFILES

@login_required
def perfil(request):
    usuario=request.user
    
    context={"usuarios": usuario, "avatar":verAvatar(request)}
    return render(request, "AppClientes/perfil.html", context)

#class perfil(LoginRequiredMixin, ListView):
#    model = User
#    template_name ='AppClientes/perfil.html'
#    return render (User.objects.all())



@login_required
def perfilEditar(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppClientes/perfil.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar":verAvatar(request)})
        else:
            return render(request, "AppClientes/perfileditar.html", {"form": form, "nombreusuario":usuario.username, "avatar":verAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppClientes/perfileditar.html", {"form": form, "nombreusuario":usuario.username, "avatar":verAvatar(request)})
    

#####  MENSAJERIA




@login_required
def nuevomensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = Mensaje()
            mensaje.emisor = request.user
            mensaje.receptor = form.cleaned_data["receptor"]
            mensaje.texto = form.cleaned_data["texto"]
            mensaje.save()
            return render(request, "AppClientes/nuevomensaje.html", {"mensaje": "Mensaje enviado correctamente", "avatar":verAvatar(request)})
        else:
            return render(request, "AppClientes/nuevomensaje.html", {"form": form, "avatar":verAvatar(request)})
    else:
        form = MensajeForm()
        return render(request, "AppClientes/nuevomensaje.html", {"form": form, "avatar":verAvatar(request)})


class verInbox(LoginRequiredMixin, ListView):
    model=Mensaje
    template_name="AppClientes/inbox.html"
 
        

class verMensaje(LoginRequiredMixin, DetailView):
    model=Mensaje
    template_name="AppClientes/vermensaje.html"


######################################################################


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])#antes de guardarlo, tengo q hacer algo
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":verAvatar(request)})
        else:
            return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":verAvatar(request)})
    

