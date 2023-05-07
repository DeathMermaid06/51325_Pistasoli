from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Factura)
admin.site.register(Sabores)
admin.site.register(Mensaje)
admin.site.register(Avatar)



#@admin.register(Pedido)
#class Pedido(admin.ModelAdmin):
#    pass



