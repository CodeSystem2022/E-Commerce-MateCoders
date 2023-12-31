from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Permission, User
from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto, Categoria, Carrito
from .forms import FormProducto, Producto
from django.urls import reverse
from django.contrib.auth.decorators import permission_required, login_required
#import pywhatkit

#PHONE = '+541159528537' # número de telefono donde recibir el pedido 
def home(request):
    if "carrito" not in request.session:
            request.session["carrito"] = []
    nuevos = Producto.objects.all().order_by('-fecha')[:3]
    productos = Producto.objects.all().order_by('-fecha')[3:10]

    return render(request, 'tienda/index.html', {
        'productos': productos,
        'nuevos': nuevos,
        'carrito': request.session["carrito"]


    })


def producto(request, id_producto):

    return render(request, 'tienda/producto.html', {
        'ctx': get_object_or_404(Producto, id=id_producto),


    })


@permission_required('TIENDA.add_producto')
def agregar(request):

    data = {"form": FormProducto()}
    if request.method == "POST":
        form = FormProducto(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda:home')
        else:
            form = FormProducto()
    return render(request, "tienda/agregar.html", data)


def categoria(request, id):    
    return render(request, 'tienda/categorias.html', {
        'cat': Producto.objects.filter(categoria=id)
    })


@permission_required('TIENDA.change_producto')
def editar(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    if request.method == 'POST':
        form = FormProducto(data=request.POST,
                            files=request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('tienda:home')
    else:
        form = FormProducto(instance=producto)
        return render(request, 'tienda/editar.html', {
            'producto': producto,
            'form': form
        })


@permission_required('TIENDA.delete_producto')
def eliminar(request, articulo_id):
    producto = get_object_or_404(Producto, id=articulo_id)
    producto.delete()
    return redirect("tienda:home")


def buscar(request):
    buscar = request.GET['buscar']
    producto = Producto.objects.filter(
        Q(descripcion__icontains=buscar) | Q(titulo__icontains=buscar))

    return render(request, 'tienda/buscar.html', {

        'producto': producto,

    })


def carrito(request, id_producto):
    request.session['carrito'] += [id_producto]
    return redirect('tienda:home')
    

def checkout(request):
    productos = []
    total = 0
    for id in request.session['carrito']:
        productos.append(get_object_or_404(Producto, id=id))
        total += Producto.objects.get(id=id).precio
    print(total)        
    
    return render(request, 'tienda/carrito.html', {
        'carrito': request.session['carrito'],
        'productos': productos,
        'total': total
    })
    
def borrar_carrito(request):
    request.session['carrito'] = [] 
    return redirect("tienda:checkout")

@login_required
def confirmar_pedido(request):
    total = float((request.POST.get("total")).replace(',', '.'))
    usuario = User.objects.get(username=request.user)    
    cart = Carrito.objects.create(usuario = usuario, total = total)
    cart.save()
    for id in request.session['carrito']:        
        cart.lista.add(Producto.objects.get(id=id))
    request.session['carrito'] = []
    
    return redirect("tienda:home") 
        
        
def acerca(request):
    return render(request, 'tienda/acerca.html')

@staff_member_required
def pedidos(request):
    if request.method == 'POST':
        enviados = {k:v[0] for k,v in dict(request.POST).items()}
        enviados.pop('csrfmiddlewaretoken')
        for valor in enviados.items():
            id_pedido = valor[0]
            enviado_pedido = True if valor[1] == 'on' else False
            pedido = Carrito.objects.get(id=id_pedido)
            pedido.enviado = enviado_pedido
            pedido.save()

        pedidos = Carrito.objects.all()
        pedidos_con_productos = []
        for pedido in pedidos:
            productos = pedido.lista.all()
            pedidos_con_productos.append((pedido, productos))
        return render(request, 'tienda/pedidos.html', {'pedidos': pedidos_con_productos})
    else:
        pedidos = Carrito.objects.all()
        pedidos_con_productos = []
        for pedido in pedidos:
            productos = pedido.lista.all()
            pedidos_con_productos.append((pedido, productos))
        return render(request, 'tienda/pedidos.html', {'pedidos': pedidos_con_productos})