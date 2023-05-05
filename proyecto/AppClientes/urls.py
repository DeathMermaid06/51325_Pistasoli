from django.urls import path
from .views import *
from AppMain.urls import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicioAppClientes, name="InicioAppClientes"),

    path('facturas/', facturas, name="facturas"),
    path('precios/', precios, name="precios"),
    path('inbox/', inbox, name="inbox"),
    path('nuevomensaje/', nuevomensaje, name="nuevomensaje"),

    path('preciosborrar/<id>', preciosborrar, name="preciosborrar"),
    path('precioseditar/<id>', precioseditar, name="precioseditar"),

    path('loginregisterC/', loginregisterC, name="loginregisterC"),    
    path('registerC/', registerC, name="registerC"),
    path('logout/', LogoutView.as_view(template_name='AppClientes/logout.html'), name="logout"),


    path('pedidos_por_cliente/', PedidoPorUsuario.as_view(template_name='AppClientes/pedidos_por_cliente.html'), name="pedidos_por_cliente"),
    path('pedidos_super/', vista_super, name="pedidos_super"),
  

]





