from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# Create your views here.

def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/inicio.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'tienda/detalle.html', {'producto': producto})

def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    carrito[str(producto_id)] = carrito.get(str(producto_id), 0) + 1
    request.session['carrito'] = carrito
    return redirect('inicio')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, pk=id)
        subtotal = producto.precio * cantidad
        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
        total += subtotal

    return render(request, 'tienda/carrito.html', {
        'productos_carrito': productos,
        'total': total
    })

def vaciar_carrito(request):
    request.session['carrito'] = {}
    return redirect('ver_carrito')

def finalizar_compra(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, pk=id)
        subtotal = producto.precio * cantidad
        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
        total += subtotal

    return render(request, 'tienda/finalizar.html', {
        'productos_carrito': productos,
        'total': total
    })

def confirmacion_pedido(request):
    request.session['carrito'] = {}
    return render(request, 'tienda/confirmacion.html')