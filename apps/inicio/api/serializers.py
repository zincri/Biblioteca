from apps.inicio.models import Autor,Libro,Prestador,Portada,Editorial,Categoria,DetallePrestamo
from rest_framework import serializers

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('__all__')

class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ('__all__')
class PortadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portada
        fields = ('__all__')

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('__all__')

class DetallePrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePrestamo
        fields = ('__all__')