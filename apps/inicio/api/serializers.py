from apps.inicio.models import Autor,Libro,Prestador,Portada,Editorial,Categoria,DetallePrestamo
from rest_framework import serializers

class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('__all__')

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class LibroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('__all__')

class PrestadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ('__all__')
class PortadaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Portada
        fields = ('__all__')

class EditorialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('__all__')

class DetallePrestamoSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetallePrestamo
        fields = ('__all__')