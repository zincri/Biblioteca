from rest_framework import viewsets
from  apps.inicio.api.serializers import AutorSerializer,CategoriaSerializer,PrestadorSerializer,PortadaSerializer,LibroSerializer,EditorialSerializer,DetallePrestamoSerializer,UserSerializer
from apps.inicio.models import Autor,Libro,Prestador,Portada,Editorial,Categoria,DetallePrestamo
from django.contrib.auth.models import User
class LibroViewSet(viewsets.ModelViewSet):
    serializer_class= LibroSerializer
    queryset = Libro.objects.all()
    
class PrestadorViewSet(viewsets.ModelViewSet):
    serializer_class= PrestadorSerializer
    queryset = Prestador.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= CategoriaSerializer
    queryset = Categoria.objects.all()

class AutorViewSet(viewsets.ModelViewSet):
    serializer_class= AutorSerializer
    queryset = Autor.objects.all()

class PortadaViewSet(viewsets.ModelViewSet):
    serializer_class= PortadaSerializer
    queryset = Portada.objects.all()

class DetallePrestamoViewSet(viewsets.ModelViewSet):
    serializer_class= DetallePrestamoSerializer
    queryset = DetallePrestamo.objects.all()

class EditorialViewSet(viewsets.ModelViewSet):
    serializer_class= EditorialSerializer
    queryset = Editorial.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
