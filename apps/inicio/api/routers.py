from rest_framework import routers
from . import viewsets as viewset


router = routers.DefaultRouter()
router.register(r'libros',viewset.LibroViewSet,base_name='list-libros')
router.register(r'prestadores',viewset.PrestadorViewSet,base_name='list-prestador')
router.register(r'categorias',viewset.CategoriaViewSet,base_name='list-categoria')
router.register(r'autores',viewset.AutorViewSet,base_name='list-autor')
router.register(r'editoriales',viewset.EditorialViewSet,base_name='list-editoriales')
router.register(r'portadas',viewset.PortadaViewSet,base_name='list-portadas')
router.register(r'detalle_prestamos',viewset.DetallePrestamoViewSet,base_name='list-prestamos')
router.register(r'users', viewset.UserViewSet)
router.register(r'libro-prestado', viewset.LibroPrestadoViewSet,base_name='get-libro-prestado')
