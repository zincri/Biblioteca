from apps.inicio.models import Autor,Libro,Prestador,Portada,Editorial,Categoria,DetallePrestamo
from rest_framework import serializers

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    #libros = LibroSerializer(many=True)
    class Meta:
        model = Categoria
        fields = ('__all__')
    """def create(self, validated_data):
        categoria = Categoria( nombre_categoria=validated_data.get("nombre") )
        categoria.save()        
        libros = validated_data.get('libros')
        for libro in libros:
          Libro.objects.create(categoria=categoria, **libro)
        return validated_data"""

class LibroSerializer(serializers.ModelSerializer):
    #categoria = CategoriaSerializer(many=True)
    categoria = CategoriaSerializer(read_only=True)
    categoriaId = serializers.PrimaryKeyRelatedField(write_only=True,
                                                queryset=Categoria.objects.all(),
                                                 source='categoria')
    class Meta:
        model = Libro
        fields = ('__all__')
    """def create(self, validated_data):
        libro = Libro( nombre=validated_data.get("nombre") )
        libro.anio_publicacion=validated_data.get("anio_publicacion")
        libro.estado_prestado=validated_data.get("estado_prestado")
        libro.activo=validated_data.get("activo")
        -----------
        libro.categoria = validated_data.get('categoria')
        libro.save() 
        return validated_data
        """

        

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