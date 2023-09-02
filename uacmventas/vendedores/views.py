from django.shortcuts import render
from django.shortcuts import render
from .models import Vendedor, HorarioDisponible

def lista_vendedores(request):
    vendedores = Vendedor.objects.all().order_by('-prioridad') 
    return render(request, 'vendedores/lista_vendedores.html', {'vendedores': vendedores})

def detalle_vendedor(request, vendedor_id):
    vendedor = Vendedor.objects.get(pk=vendedor_id)
    horarios = HorarioDisponible.objects.filter(vendedor=vendedor)
    articulos = vendedor.articulo_set.all()
    return render(request, 'vendedores/detalle_vendedor.html', {'vendedor': vendedor, 'articulos': articulos, 'horarios':horarios})

