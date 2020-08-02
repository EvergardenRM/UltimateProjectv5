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
def about(request,):
    return render(request,"about.html")
def bodega(request,):
    return render(request,"bodega.html")
def contact(request,):
    return render(request,"contact.html")
def producto_cliente(request,):
    return render(request,"producto_cliente.html")
def recibo_factura(request,):
    return render(request,"recibo_factura.html")


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
