from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicioAppMain(request):
    return render(request, "AppMain/index.html")

def about(request):
    return render(request, "AppMain/about.html")

def sabores(request):
    return render(request, "AppMain/sabores.html")

def ingresar(request):
    return render(request, "AppMain/loginregister.html")
