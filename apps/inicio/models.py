from django.db import models
from django.contrib.auth.models import User



# Create your models here.
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
    def __str__(self):
        return str(self.id)+" - "+self.nombre_categoria

class Editorial(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null=True)
    direccion = models.CharField(max_length=100,blank=True,null=True)
    codigo_postal = models.CharField(max_length=100,blank=True,null=True)
    telefono = models.CharField(max_length=15,blank=True,null=True)
    correo = models.CharField(max_length=50,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    
    def __str__(self):
        return str(self.id)+" - "+self.nombre
    
class Libro(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null=True)
    anio_publicacion = models.DateField(auto_now_add=True,blank=True,null=True)
    estado_prestado = models.BooleanField(default=False,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    stock = models.IntegerField(default=0,blank=True,null=True)
    categoria = models.ForeignKey(Categoria,blank=True,null=True,
                                    on_delete=models.CASCADE,
                                    related_name='libros',
                                    verbose_name="categoria")
    editorial = models.ForeignKey(Editorial,blank=True,
                                            null=True,
                                            on_delete=models.CASCADE,
                                            related_name='editorial')
    autor = models.ForeignKey(Autor,blank=True,
                                            null=True,
                                            on_delete=models.CASCADE,
                                            related_name='autor')
    
    def __str__(self):
        return str(self.id)+" - "+self.nombre

class Prestador(User):
    telefono = models.CharField(max_length=15,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    libro = models.ManyToManyField(Libro, through="DetallePrestamo")
    def __str__(self):
        return str(self.id)+" - "+self.username
    def name(self):
        return str(self.username)

class Portada(models.Model):
    url = models.CharField(max_length=1000,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    libro = models.OneToOneField(Libro,blank=True,null=True,on_delete=models.CASCADE,related_name='portada')
    def __str__(self):
        return str(self.id)+" - "+self.url


class DetallePrestamo(models.Model):
    #auto_now_add=True esa propiedad quita la fecha de donde lo puse
    fecha_inicio = models.DateField(auto_now_add=True,blank=True,null=True)
    fecha_vencimiento = models.DateField(auto_now_add=True,blank=True,null=True)
    activo = models.BooleanField(default=True,blank=True,null=True)
    prestador = models.ForeignKey(Prestador,blank=True,null=True,on_delete=models.CASCADE,related_name='prestador')
    libro = models.ForeignKey(Libro,blank=True,null=True,on_delete=models.CASCADE,related_name='libro')
    def __str__(self):
        return str(self.id)+" - "+self.fecha_inicio

