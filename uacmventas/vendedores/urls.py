from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vendedores, name='lista_vendedores'),
    path('<int:vendedor_id>/', views.detalle_vendedor, name='detalle_vendedor'),
]
