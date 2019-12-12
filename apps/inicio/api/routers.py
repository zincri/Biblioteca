from rest_framework import routers
from . import viewsets as viewset

router = routers.DefaultRouter()
router.register(r'libros',viewset.LibroViewSet,base_name='list-libros')
router.register(r'prestador',viewset.PrestadorViewSet,base_name='list-prestador')
router.register(r'categoria',viewset.CategoriaViewSet,base_name='list-categoria')
