from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioAppMain, name="InicioAppMain"),
    path('about/', about, name="about"),
    path('sabores/', sabores, name="sabores"),

]




