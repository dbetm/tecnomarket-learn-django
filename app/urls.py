from django.urls import path, include
from rest_framework import routers

from .views import home, contacto, galeria, scan
from .views import (
    agregar_producto,
    listar_productos,
    modificar_producto,
    eliminar_producto,
    registro
)
from .views import MarcaViewset, ProductoViewset

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)


urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('scan/', scan, name='scan'),
    path('galeria/', galeria, name='galeria'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),
]
