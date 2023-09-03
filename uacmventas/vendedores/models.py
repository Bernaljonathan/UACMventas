from django.db import models



class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=False, default="sample@gmail.com")
    titulo = models.CharField(max_length=200,default='Tu producto')
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='vendedores/', null=False)
    prioridad = models.IntegerField(default=0)
    numero_whatsapp = models.CharField(max_length=20, null=False)
    comentario = models.TextField(blank= True)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='articulos/')


    def __str__(self):
        return self.nombre



class HorarioDisponible(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.dia_semana} - {self.hora_inicio} a {self.hora_fin}"
