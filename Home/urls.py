from django.urls import path
from .views import *

urlpatterns = [
    path('biografia/', vista_about, name = 'vista_about'),
    path('motos/', vista_motos, name = 'vista_motos'),
    path('empresas/', vista_empresas, name = 'vista_empresas'),
    path('empleados/', vista_empleado, name = 'vista_empleado'),
    path('contacto/', vista_contacto, name = 'vista_contacto'),
    path('formulario/', vista_formulario, name = 'formulario'),
    path('lista_producto/', vista_lista_producto, name = 'vista_lista_producto'),
    path('lista_categoria/', vista_lista_categoria, name = 'vista_lista_categoria'),
    path('lista_marca/', vista_lista_marca, name = 'vista_lista_marca'),
    path('agregar_producto/', vista_agregar_producto, name = 'vista_agregar_producto'),
    path('agregar_categoria/', vista_agregar_categoria, name = 'vista_agregar_categoria'),
    path('ver_producto/<int:id_prod>/', vista_ver_producto, name = 'vista_ver_producto'),
    path('editar_producto/<int:id_prod>/', vista_editar_producto, name = 'vista_editar_producto'),
    path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto, name= 'vista_eliminar_producto'),
    path('administracion/', vista_administracion, name = 'vista_administracion'),
    path('login/', vista_login, name = 'vista_login'),
    path('logout/', vista_logout, name = 'vista_logout'),
    path('registrar/', vista_registrar, name = 'vista_registrar'),
    path('ws/productos',ws_productos_vista, name = 'ws_productos_vista'),
    path('base/',vista_base, name ='vista_base'),
   ]
