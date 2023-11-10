from django.contrib import admin
from .models import Producto, Carrito, Categoria 

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'precio',)
    search_fields = ('titulo',)
    list_filter = ('categoria',)

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'enviado',)
    search_fields = ('usuario',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)