from django.contrib import admin
from .models import Producto, Carrito, Categoria 


admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Categoria)