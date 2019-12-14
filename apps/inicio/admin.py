from django.contrib import admin
from apps.inicio.models import Prestador,Categoria, Portada, DetallePrestamo, Libro, Editorial,Autor
# Register your models here.
admin.site.register(Prestador)
admin.site.register(Categoria)
admin.site.register(Portada)
admin.site.register(DetallePrestamo)
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Autor)