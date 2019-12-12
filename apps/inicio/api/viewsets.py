from rest_framework import viewsets
from  apps.inicio.api.serializers import AutorSerializer,CategoriaSerializer,PrestadorSerializer,PortadaSerializer,LibroSerializer,EditorialSerializer,DetallePrestamoSerializer
from apps.inicio.models import Autor,Libro,Prestador,Portada,Editorial,Categoria,DetallePrestamo

class LibroViewSet(viewsets.ModelViewSet):
    serializer_class= LibroSerializer
    queryset = Libro.objects.all()
    
class PrestadorViewSet(viewsets.ModelViewSet):
    serializer_class= PrestadorSerializer
    queryset = Prestador.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= CategoriaSerializer
    queryset = Categoria.objects.all()
