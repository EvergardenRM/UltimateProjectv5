from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from  django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages
from UltimateProjectv5.forms import RegisterForm
from django.contrib.auth.models import User
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
def login_view(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username)
        #print(password)

        user = authenticate(username=username , password=password)
        if user:
            print('usuario auntenticado')
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('home')

        else:
            print('usuario no auntenticado')
            messages.error(request,'Usuario o Contraseña no  Valida')


    return render(request,"Login.html",{})

def logout_view(request):
    logout(request)
    messages.error(request,'sesion ha sido cerrado satisfactorios')
    return redirect('login')
def register(request):
    form = RegisterForm(request.POST or None)  # valida  que si hay elementos post
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username,email,password)
        #user =form.save()
        if user:
            login(request,user)
            messages.success(request, 'Usuario  Creado correctamente')
            return redirect('home')

        print('Username',username)
        print('email',email)
        print('password',password)


    return render(request,'Forms_register.html',{'form':form})




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
