from apps.inicio.models import Autor,Libro,Prestador,Portada,Editorial,Categoria,DetallePrestamo
from rest_framework import serializers
from django.contrib.auth.models import User

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
class PortadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portada
        fields = ('__all__')

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('__all__')

class LibroSerializer(serializers.ModelSerializer):
    portada = PortadaSerializer(read_only=True)
    editorial = EditorialSerializer(read_only=True)
    editorialId = serializers.PrimaryKeyRelatedField(write_only=True,
                                                queryset=Editorial.objects.all(),
                                                 source='editorial')
    categoria = CategoriaSerializer(read_only=True)
    categoriaId = serializers.PrimaryKeyRelatedField(write_only=True,
                                                queryset=Categoria.objects.all(),
                                                 source='categoria')
    autor = AutorSerializer(read_only=True)
    autorId = serializers.PrimaryKeyRelatedField(write_only=True,
                                                queryset=Autor.objects.all(),
                                                 source='autor')
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
    libro = LibroSerializer(many=True)
    class Meta:
        model = Prestador
        fields = ('__all__')


class DetallePrestamoSerializer(serializers.ModelSerializer):
    libro = LibroSerializer(read_only=True)
    prestador = PrestadorSerializer(read_only=True)
    libroId = serializers.PrimaryKeyRelatedField(write_only=True,
                                                queryset=Libro.objects.all(),
                                                 source='libro')
    prestadorId = serializers.PrimaryKeyRelatedField(write_only=True,
                                                queryset=Prestador.objects.all(),
                                                 source='prestador')
                                                 
    class Meta:
        model = DetallePrestamo
        fields = ('__all__')
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class DetalleLibroPrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePrestamo
        fields = ('__all__')

    def create(self, validated_data):
        libro = validated_data.get("libro")
        libro.stock = libro.stock - 1
        libro.save()
        
        dp = DetallePrestamo()
        dp.prestador = validated_data.get("prestador") 
        dp.libro = validated_data.get("libro")
        dp.activo = True
        dp.save()
        return validated_data
    def update(self, instance, validated_data):
        print(instance.libro.stock + 1)
        libro = Libro.objects.get(id=instance.libro.id)
        libro.stock = instance.libro.stock + 1
        libro.save()

        #instance.libro.stock = int(instance.libro.stock + 1) 
        instance.activo = validated_data.get('activo', instance.activo)
        instance.save()
        return instance