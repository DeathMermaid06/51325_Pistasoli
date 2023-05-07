from django.urls import path
from .views import *
from AppClientes.views import *

urlpatterns = [
    path("", inicioAppMain, name="InicioAppMain"),
    path('about/', about, name="about"),
    path('sabores/', sabores, name="sabores"),
    path('pages/', pages, name="pages"),

]




