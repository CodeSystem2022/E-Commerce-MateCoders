from .models import Categoria, Producto


def extras(request):
    if "carrito" not in request.session:
        request.session["carrito"] = []
    cantidad_productos = len(request.session['carrito'])
    return({'categoria': Categoria.objects.all(),
            'cantidad_productos': cantidad_productos,
            })
        
