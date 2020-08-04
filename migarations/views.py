from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
# Create your views here.



# Create your views here.

def home(request,):
    return render(request,'base.html')

def inicio(request):
    return render(request,'caja.html')

def about(request, plantilla="about.html"):
    return render(request, plantilla)

def cliente(request,):
    return render(request,"Clientes.html")

def bodega(request,):
    return render(request,"bodega.html")
def contact(request,):
    return render(request,"contact.html")
def producto_cliente(request,):
    return render(request,"producto_cliente.html")
def recibo_factura(request,):
    return render(request,"recibo_factura.html")
def factura(request,):
    return render(request,"factura.html")
def ingresar_clientes(request,):
    return render(request,"ingresar_cliente.html")
def producto_caja(request,):
    return render(request,"producto_caja.html")
def entradas(request,):
    return render(request,"entrada_mercaderia.html")
def salidas(request,):
    return render(request,"salida_mercaderia.html")
def producto_bodega(request,):
    return render(request,"producto_bodega.html")

def help_bodega(request,):
    return render(request,"help.html")
def help_caja(request,):
    return render(request,"help_consulta_fact.html")
def administrador(request,):
    return render(request,"administrador.html")














def telf(request,plantilla="Ingreso_Fact_help.html"):
    return render(request,plantilla)
def help(request, plantilla="help.html"):

    return render(request,plantilla)
def help_ing_fact(request, plantilla="Ingreso_Fact_help.html"):

    return render(request,plantilla)
def help_imp_fact(request, plantilla="help_imprimir_fact.html"):

    return render(request,plantilla)
def help_consult_fact(request, plantilla="help_consulta_fact.html"):

    return render(request,plantilla)
def index(request, plantilla="index.html"):

    return render(request,plantilla)
