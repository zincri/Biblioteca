from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prestador(User):
    telefono = models.CharField(max_length=15,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    def __str__(self):
        return str(self.id)+" - "+self.username
    def name(self):
        return str(self.username)
class Autor(User):
    telefono = models.CharField(max_length=15,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    def __str__(self):
        return str(self.id)+" - "+self.username
    def name(self):
        return str(self.username)

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    

class Libro(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null=True)
    anio_publicacion = models.CharField(max_length=10,blank=True,null=True)
    estado_prestado = models.BooleanField(default=False,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    categoria_id = models.ForeignKey(Categoria,blank=True,null=True,on_delete=models.SET_NULL)

class Portada(models.Model):
    url = models.CharField(max_length=1000,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    libro_id = models.ForeignKey(Libro,blank=True,null=True,on_delete=models.SET_NULL)

class Editorial(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null=True)
    direccion = models.CharField(max_length=100,blank=True,null=True)
    codigo_postal = models.CharField(max_length=100,blank=True,null=True)
    telefono = models.CharField(max_length=15,blank=True,null=True)
    correo = models.CharField(max_length=50,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    libro_id = models.ForeignKey(Libro,blank=True,null=True,on_delete=models.SET_NULL)
class DetallePrestamo(models.Model):
    fecha_inicio = models.CharField(max_length=100,blank=True,null=True)
    fecha_vencimiento = models.CharField(max_length=100,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    prestador_id = models.ForeignKey(Prestador,blank=True,null=True,on_delete=models.SET_NULL)
    libro_id = models.ForeignKey(Libro,blank=True,null=True,on_delete=models.SET_NULL)