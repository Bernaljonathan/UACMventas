from vendedores.models import Categoria

def categorias (request):
    #Obtener la lista de categorias desde la DB
    categorias = Categoria.objects.all()
    return {'categorias': categorias}