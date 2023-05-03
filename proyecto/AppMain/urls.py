from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioAppMain, name="InicioAppMain"),
    path('about/', about, name="about"),
    path('sabores/', sabores, name="sabores"),
    path('ingresar/', ingresar),
    path('registar/', registrar),
    path('perfil/', perfil),

    path('crear_sabores/', crear_sabores),
]




