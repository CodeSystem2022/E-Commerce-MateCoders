from django.urls import path
from . import views


app_name = 'tienda'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('producto/<int:id_producto>', views.producto, name = 'producto'),
    path('agregar/', views.agregar, name = 'agregar'),
    path('categoria/<int:id>', views.categoria, name = 'categorias'),
    path('editar/<int:id_producto>', views.editar, name = 'editar'),
    path('eliminar/<articulo_id>', views.eliminar, name = 'eliminar'),
    path('buscar/', views.buscar, name = 'buscar'),
    path('carrito/<int:id_producto>', views.carrito, name = 'carrito'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('borrar_carrito/', views.borrar_carrito, name ='borrar_carrito'),
    path('confirmar/', views.confirmar_pedido, name= 'confirmar_pedido'),
    path('acerca/', views.acerca, name = 'acerca'),
]
