from django.shortcuts import render, redirect
from .models import Vendedor, HorarioDisponible
from .forms import VendedorForm, ArticuloForm

def lista_vendedores(request):
    vendedores_activos = Vendedor.objects.filter(activo=True).order_by('-prioridad')
    return render(request, 'vendedores/lista_vendedores.html', {'vendedores': vendedores_activos, 'activo': True})

def detalle_vendedor(request, vendedor_id):
    vendedor = Vendedor.objects.get(pk=vendedor_id)
    horarios = HorarioDisponible.objects.filter(vendedor=vendedor, horario_activo =True)
    articulos = vendedor.articulo_set.all() 
    return render(request, 'vendedores/detalle_vendedor.html', {'vendedor': vendedor, 'articulos': articulos, 'horarios':horarios})

def crear_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST, request.FILES)
        if form.is_valid():
            vendedor = form.save(commit=False)
            vendedor.activo = False  # Define el vendedor como inactivo hasta su aprobación.
            vendedor.save()
            return redirect('lista_vendedores')  # Puedes redirigir a donde sea necesario.
    else:
        form = VendedorForm()

    return render(request, 'crear_vendedor.html', {'form': form})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.aprobado = False  # Define el artículo como no aprobado hasta su revisión.
            articulo.save()
            return redirect('detalle_vendedor')  # Puedes redirigir a donde sea necesario.
    else:
        form = ArticuloForm()

    return render(request, 'crear_articulo.html', {'form': form})