from rest_framework import viewsets
from  apps.inicio.api.serializers import AutorSerializer,CategoriaSerializer,PrestadorSerializer,PortadaSerializer,LibroSerializer,EditorialSerializer,DetallePrestamoSerializer,UserSerializer,DetalleLibroPrestamoSerializer
from apps.inicio.models import Autor,Libro,Prestador,Portada,Editorial,Categoria,DetallePrestamo
from django.contrib.auth.models import User
class LibroViewSet(viewsets.ModelViewSet):
    serializer_class= LibroSerializer
    queryset = Libro.objects.filter(activo=True)
    
class PrestadorViewSet(viewsets.ModelViewSet):
    serializer_class= PrestadorSerializer
    queryset = Prestador.objects.filter(activo=True)

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= CategoriaSerializer
    queryset = Categoria.objects.filter(activo=True)

class AutorViewSet(viewsets.ModelViewSet):
    serializer_class= AutorSerializer
    queryset = Autor.objects.filter(activo=True)

class PortadaViewSet(viewsets.ModelViewSet):
    serializer_class= PortadaSerializer
    queryset = Portada.objects.filter(activo=True)

class DetallePrestamoViewSet(viewsets.ModelViewSet):
    serializer_class= DetallePrestamoSerializer
    queryset = DetallePrestamo.objects.filter(activo=True)

class EditorialViewSet(viewsets.ModelViewSet):
    serializer_class= EditorialSerializer
    queryset = Editorial.objects.filter(activo=True)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Este serializador es un servicio del api aparte,
#me sirve para saber si ya existe prestado el libro 
#con el mismo usuario.
class LibroPrestadoViewSet(viewsets.ModelViewSet):
    queryset = DetallePrestamo.objects.filter(activo=True)
    serializer_class = DetalleLibroPrestamoSerializer

