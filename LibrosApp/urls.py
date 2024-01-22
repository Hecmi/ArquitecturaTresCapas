
from django.urls import path
from .views import *

urlpatterns = [
    path('agregarcliente/', agregarcliente, name='agregarcliente'),
    path('agregarsucursales/', agregarsucursales, name='agregarsucursales'),
    path('producto_sucursales/',producto_sucursales, name='producto_sucursales'),
    path('ver_producto_sucursales/',ver_producto_sucursales, name='ver_producto_sucursales'),
    path('ver_cliente/', ver_cliente, name='ver_cliente'),
    path('ver_sucursales/', ver_sucursales, name='ver_sucursales'),
    path('buscar_cliente/', buscar_cliente, name='buscar_cliente'),  # Añade esta línea para la búsqueda
    path('buscar_producto/', buscar_producto, name='buscar_producto'),  # Añade esta línea para la búsqueda
    path('buscar_sucursal/', buscar_sucursal, name='buscar_sucursal'),  # Añade esta línea para la búsqueda
    path('sucursal/editar_sucursal/<int:id_sucursal>/', editar_sucursal, name='editar_sucursal'),
    path('sucursal/eliminar/<id_sucursal>', eliminar_sucursal, name='eliminar_sucursal'),
    path('cliente/editar_cliente/<identificacion>/', editar_cliente, name='editar_cliente'),
    path('cliente/eliminar/<identificacion>', eliminar_cliente, name='eliminar_cliente'),
    path('producto/editar_producto_sucursales/<int:id_producto_sucursal>/', editar_producto_sucursales, name='editar_producto_sucursales'),
    path('producto/eliminar/<id_producto_sucursal>', eliminar_producto, name='eliminar_producto')


]
