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

from django.urls import path
from migarations import views

urlpatterns = [
    path('', views.home, name="home"),
    path('inicio/', views.inicio, name="caja"),
    path('cliente/', views.cliente, name="cliente"),
    path('bodega/', views.bodega, name="bodega"),
    path('telf/', views.telf, name="telf"),
    path('help/', views.help, name="help"),
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name="contacto"),
    path('producto_cliente/', views.producto_cliente, name="producto_cliente"),
    path('about/', views.about, name="about"),
    path('fact/', views.recibo_factura, name="cliente_facturas"),





]
