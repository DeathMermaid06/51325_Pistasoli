from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioAppClientes, name="InicioAppClientes"),
    path('pedidos/', pedidos, name="pedidos"),
    path('facturas/', facturas, name="facturas"),
    path('precios/', precios, name="precios"),
    path('inbox/', inbox, name="inbox"),
    path('nuevomensaje/', nuevomensaje, name="nuevomensaje"),

    path('preciosborrar/<id>', preciosborrar, name="preciosborrar"),
    path('precioseditar/<id>', precioseditar, name="precioseditar"),
]





