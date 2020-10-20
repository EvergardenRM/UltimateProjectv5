"""UltimateProjectv5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from migarations import views


urlpatterns = [
    
    path('inicio/', views.inicio, name="caja"),
    path('cliente/', views.cliente, name="cliente"),
    path('bodega/', views.bodega, name="bodega"),
    path('contact/', views.contact, name="contacto"),
    path('producto_cliente/', views.producto_cliente, name="producto_cliente"),
    path('about/', views.about, name="about"),
    path('fact/', views.recibo_factura, name="cliente_facturas"),
    path('ingresar_cliente/', views.ingresar_clientes, name="ingresar_factura"),
    path('producto_caja/', views.producto_caja, name="producto_caja"),
    path('entrada_mercaderia/', views.entradas, name="entrada_producto"),
    path('salida_productos/', views.salidas, name="salida_producto"),
    path('salida_bodega/', views.producto_bodega, name="producto_bodega"),
    path('help_bodega/', views.help_bodega, name="help_bodega"),
    path('help_caja/', views.help_caja, name="help_caja"),
    path('administrador/', views.administrador, name="administrador"),
    path('logout/', views.logout_view, name="logout"),
    path('admin/', admin.site.urls),
    path('', views.login_view , name="login"),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('crear_cliente/', views.crearcliente, name="crearcliente"),
    path('modificar_cliente/<int:pk>', views.modificarcliente, name="modificar_cliente"),
    path('eliminar_cliente/<int:pk>', views.eliminarcliente, name="eliminar_cliente"),
    path('crear_producto/', views.crearproducto, name="crear_producto"),
    path('modificar_producto/<int:pk>', views.modificarproducto, name="modificar_producto"),
    path('eliminar_producto/<int:pk>', views.eliminarproducto, name="eliminar_producto"),
    path('crear_marca/', views.crearmarca, name="crear_marca"),
    path('modificar_marca/<int:pk>', views.modificarmarca, name="modificar_marca"),
    path('marca/', views.marca, name="marca"),
    path('eliminar_marca/<int:pk>', views.eliminarmarca, name="eliminar_marca"),
    path('factura_principal/' ,  views.FacturaListView.as_view() , name="principal_factura"),
    path('factura/' ,  views.Detalle_facturaCreateView.as_view() , name="crear_factura"),
    path('crear_entrada/' ,  views.crear_entrada , name="crear_entrada"),
    path('modificar_entrada/<int:pk>' ,  views.modificar_entrada , name="modificar_entrada"),
    path('eliminar_entrada/<int:pk>' ,  views.eliminar_entrada , name="eliminar_entrada"),
    path('update_factura/<int:pk>' ,  views.Detalle_facturaUpdateView.as_view() , name="update_factura"),
    path('delete_factura/<int:pk>' ,  views.Detalle_facturaDeleteView.as_view() , name="delete_factura"),
    path('eliminar_factura/<int:pk>' ,  views.Eliminar_facturaUpdateView.as_view() , name="eliminar_factura"),
    path('crear_salida/' ,  views.crear_salida , name="crear_salida"),
    path('modificar_salida/<int:pk>' ,  views.modificar_salida , name="modificar_salida"),
    path('eliminar_salida/<int:pk>' ,  views.eliminar_salida , name="eliminar_salida"),
    path('prueba_marca/<int:pk>' ,  views.prueba , name="prueba"),
    path('prueba_2/<int:pk>' ,  views.crear_detalles , name="detalles_f"),
    path('crear_rol/' ,  views.crear_rol , name="crear_rol"),
    path('permisos_usuarios/' ,  views.crear_rol_usuario , name="crear_permisos"),
    path('usuario/' ,  views.usuario , name="usuario"),
    path('crear_usuario/' ,  views.crear_usuario , name="crear_usuario"),
    path('modificar_usuario/<int:pk>' ,  views.modificar_usuario , name="modificar_usuario"),
    path('modificar_rol/<int:pk>' ,  views.modificar_rol , name="modificar_rol"),
    path('eliminar_rol/<int:pk>' ,  views.eliminar_rol , name="eliminar_rol"),
    path('rol/' ,  views.rol , name="rol"),
    path('rol_usuario/' ,  views.rol_usuario , name="rol_usuario"),
    path('modificar_rol_usuario/<int:pk>' ,  views.modificar_rol_usuario , name="modificar_rol_usuario"),
    path('eliminar_rol_usuario/<int:pk>' ,  views.eliminar_rol_usuario , name="eliminar_rol_usuario"),
    path('pdf_factura/' ,  views.pdf_factura , name="pdf_factura"),
    path('pdf_cliente/' ,  views.pdf_cliente, name="pdf_cliente"),
    path('pdf_producto/' ,  views.pdf_producto, name="pdf_producto"),
    path('pdf_marca/' ,  views.pdf_marca, name="pdf_marca"),
    path('modificar_detalles/<int:pk>' ,  views.modificar_detalles , name="modificar_detalles"),
    path('eliminar_detalles/<int:pk>' ,  views.eliminar_detalles , name="eliminar_detalles"),
    
]


