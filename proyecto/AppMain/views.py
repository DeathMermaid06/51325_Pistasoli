from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def inicioAppMain(request):
    return render(request, "AppMain/index.html")

def about(request):
    return render(request, "AppMain/about.html")

def sabores(request):
    return render(request, "AppMain/sabores.html")

def ingresar(request):
    return render(request, "AppMain/loginregister.html")




def registrar(request):
    return HttpResponse("REGISTRAR FUNCA")

def perfil(request):
    return HttpResponse("PERFIL FUNCA")


def crear_sabores(request):
    return HttpResponse("CREAR SABORES FUNCA")