from django import forms
from .models import Vendedor, Articulo

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'email', 'titulo','descripcion', 'imagen', 'numero_whatsapp', 'comentario']
    
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
        