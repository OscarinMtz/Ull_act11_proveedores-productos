from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm

# Vistas para Proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Crear Proveedor'})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('app_productos:detalle_proveedor', proveedor_id=proveedor.id)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Editar Proveedor'})

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('app_productos:listar_proveedores')
    return render(request, 'confirmar_borrar.html', {'objeto': proveedor, 'tipo': 'proveedor'})

# Vistas para Productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('app_productos:detalle_producto', producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Editar Producto'})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('app_productos:listar_productos')
    return render(request, 'confirmar_borrar.html', {'objeto': producto, 'tipo': 'producto'})

def inicio(request):
    proveedores_count = Proveedor.objects.count()
    productos_count = Producto.objects.count()
    return render(request, 'inicio.html', {
        'proveedores_count': proveedores_count,
        'productos_count': productos_count
    })