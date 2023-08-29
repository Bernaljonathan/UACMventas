from django.contrib import admin
from .models import Vendedor, Articulo, HorarioDisponible

admin.site.register(Vendedor)
admin.site.register(Articulo)
admin.site.register(HorarioDisponible)