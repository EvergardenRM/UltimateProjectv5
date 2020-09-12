from django.shortcuts import render,  HttpResponse
from django.http import  HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render,  HttpResponse, redirect, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from  django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages
from UltimateProjectv5.forms import *
from django.contrib.auth.models import User
from .models import Cliente, Producto
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy 

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
@login_required(login_url='/')
def ingresar_clientes(request,plantilla= "ingresar_cliente.html"):
    busqueda = request.GET.get("buscar")
    clientes = list(Cliente.objects.filter(estado = 1))
    if busqueda:
        clientes = list(Cliente.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(cedula__icontains = busqueda) |
            Q(apellido__icontains = busqueda)|
            Q(email__icontains = busqueda)|
            Q(edad__icontains = busqueda)
            ).distinct())
    else:
        return render(request, plantilla, {'clientes': clientes})
    return render(request, plantilla, {'clientes': clientes})
@login_required(login_url='/')
def producto_caja(request,plantilla= "producto_caja.html"):
    productos = list(Producto.objects.filter(estado = 1))
    return render(request, plantilla, {'productos': productos})

def entradas(request,plantilla='entrada_mercaderia.html'):
    busqueda = request.GET.get('buscar')
    entradas = list(Entrada_producto.objects.filter(estado=1))
    if busqueda:
        entradas = list(Entrada_producto.objects.filter(
            
            Q(descripcion__icontains = busqueda) |
            Q(cantidad__icontains = busqueda) |
            Q(monto__icontains = busqueda)
            ).distinct())
    else:
        return render(request, plantilla, {'entradas': entradas})
    return render(request,plantilla,{'entradas': entradas })



def salidas(request, plantilla="salida_mercaderia.html"):
    busqueda = request.GET.get('buscar')
    salidas = list(Salida_producto.objects.filter(estado=1))
    if busqueda:
        salidas = list(Salida_producto.objects.filter(      
            Q(descripcion__icontains = busqueda) |
            Q(cantidad__icontains = busqueda) |
            Q(monto__icontains = busqueda)
            ).distinct())
    else:
        salidas = list(Salida_producto.objects.filter(estado=1))
    return render(request,plantilla,{'salidas': salidas})
    
    
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
            messages.error(request,'Usuario o Contraseña no  Valido')


    return render(request,"Login.html",{})

def logout_view(request):
    logout(request)
    messages.error(request,'La sesion ha sido cerrada satisfactoriamente')
    return redirect('login')
def register(request):
    form = RegisterForm(request.POST or None)  # valida  que si hay elementos post
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email,password)
        #user =form.save()
        if user:
            login(request,user)
            messages.success(request, 'Usuario  Creado correctamente')
            return redirect('home')

        print('Username',username)
        print('email',email)
        print('password',password)


    return render(request,'Forms_register.html',{'form':form})

def crearcliente(request, plantilla="crearcliente.html"):
    if request.method == "POST":
        formcliente = ClienteForm(request.POST or None)
        if formcliente.is_valid():
            formcliente.save()
            return redirect("ingresar_factura")
    else:
        formcliente = ClienteForm()
    return render(request, plantilla, {'formcliente': formcliente})

def modificarcliente(request, pk ,plantilla="modificarcliente.html"):
    if request.method == "POST":
        cliente = get_object_or_404(Cliente, pk=pk)
        formcliente = ClienteForm(request.POST or None, instance=cliente)


        if formcliente.is_valid():
            formcliente.save()
            return redirect("ingresar_factura")
    else:
        cliente = get_object_or_404(Cliente, pk=pk)
        formcliente = ClienteForm(request.POST or None, instance=cliente)
    return render(request, plantilla, {'formcliente': formcliente})
def eliminarcliente(request, pk, plantilla="eliminarcliente.html"):
    if request.method == "POST":
        estado = Cliente.objects.get(pk=pk)
        estado.estado = 0 
        cliente = get_object_or_404(Cliente, pk=pk)
        formCliente = ClienteForm(request.POST or None, instance=cliente)
        if formCliente.is_valid():
            estado.save()
        return redirect("ingresar_factura")
    else:
        cliente = get_object_or_404(Cliente, pk=pk)
        formcliente = ClienteForm(request.POST or None, instance=cliente)


    return render(request, plantilla, {'formcliente': formcliente})


def crearproducto(request, plantilla="crearproducto.html"):
    if request.method == "POST":
        formproducto = ProductoForm(request.POST or None)
        if formproducto.is_valid():
            formproducto.save()
            return redirect("producto_caja")
    else:
        formproducto = ProductoForm()
    return render(request, plantilla, {'formproducto': formproducto})

def modificarproducto(request, pk ,plantilla="modificarproducto.html"):
    if request.method == "POST":
        producto = get_object_or_404(Producto, pk=pk)
        formproducto = ProductoForm(request.POST or None, instance=producto)
        if formproducto.is_valid():
            formproducto.save()
            return redirect("producto_caja")
    else:
        producto = get_object_or_404(Producto, pk=pk)
        formproducto = ProductoForm(request.POST or None, instance=producto)
    return render(request, plantilla, {'formproducto': formproducto})
def eliminarproducto(request, pk, plantilla="eliminarproducto.html"):
    if request.method == "POST":
        estado = Producto.objects.get(pk=pk)
        estado.estado = 0 
        producto = get_object_or_404(Producto, pk=pk)
        formProducto = ProductoForm(request.POST or None, instance=producto)
        if formProducto.is_valid():
            estado.save()
            return redirect("producto_caja")
    else:
        producto = get_object_or_404(Producto, pk=pk)
        formproducto = ProductoForm(request.POST or None, instance=producto)


    return render(request, plantilla, {'formproducto': formproducto})
def crearmarca(request, plantilla="FormMarca.html"):
    
    if request.method == "POST":
        formmarca = MarcaForm(request.POST or None)         
        if formmarca.is_valid():
            formmarca.save()
            nombre= formmarca.cleaned_data.get('nombre')
            print(nombre)
            estado = Marca.objects.get(nombre= nombre)
            print (estado.id)
            return redirect("prueba", pk= estado.id)
    else:
        formmarca = MarcaForm()
    return render(request, plantilla, {'formmarca': formmarca})

def marca(request,plantilla= "marca.html"):
    busqueda = request.GET.get("buscar")
    marca = Marca.objects.filter(estado = 1)
    if busqueda:
        marca = list(Marca.objects.filter(
            Q(nombre__icontains = busqueda)
            ).distinct())
    else:
        return render(request, plantilla, {'marca': marca})

    return render(request, plantilla, {'marca': marca})

def modificarmarca(request, pk, plantilla="elimitar_marca.html"):
    if request.method == "POST":
        marca = get_object_or_404(Marca, pk=pk)
        formmarca = MarcaForm(request.POST or None, instance=marca)       
        if formmarca.is_valid():
            formmarca.save()
            return redirect("marca")
    else:
        marca = get_object_or_404(Marca, pk=pk)
        formmarca = MarcaForm(request.POST or None, instance=marca)
    return render(request, plantilla, {'formmarca': formmarca})
def eliminarmarca(request, pk, plantilla="elimitar_marca.html"):
    if request.method == "POST":
        estado = Marca.objects.get(pk=pk)
        estado.estado = 0 
        marca = get_object_or_404(Marca, pk=pk)
        formmarca = MarcaForm(request.POST or None, instance=marca)    
        if formmarca.is_valid():             
            estado.save()
            print(estado.id)
            return redirect("marca")
    else:
        marca = get_object_or_404(Marca, pk=pk)
        formmarca = MarcaForm(request.POST or None, instance=marca)
    return render(request, plantilla, {'formmarca': formmarca})


class FacturaListView(ListView):     
    model = Cabecera_factura
    template_name = "factura.html"
    
    def get_queryset(self): 
        busqueda = self.request.GET.get("buscar")
        print (busqueda) 
        if busqueda:
            return Detalle_factura.objects.filter(   
            Q(cantidad__icontains = busqueda) 
             , estado=1 
            ).distinct()
        else:
            return Cabecera_factura.objects.filter(estado=1)
            

class Detalle_facturaCreateView(CreateView):
    model = Detalle_factura
    template_name = "crear_factura.html"
    form_class = Detalle_facturaForm
    second_form_class  = Cabecera_facturaForm

    def get_context_data(self, **kwargs):
        context = super(Detalle_facturaCreateView,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2']  = self.second_form_class(self.request.GET)
        return context
    def post(self, request,*args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            detalles = form.save(commit=False)
            detalles.cabecera_f_id = form2.save()
            detalles.save()
            nombre= form2.cleaned_data.get('codigo_factura')
            print(nombre)
            estado = Cabecera_factura.objects.get(codigo_factura= nombre)
            print (estado.id)
            valor2 = Detalle_factura.objects.filter(cabecera_f_id =estado.id)
            x= 0
            for i in valor2:
                x= 0 + i.subtotal
            print(x)
            estado.subtotal = x
            estado.save()

            return redirect("prueba", pk= estado.id)
        else:
            return self.render_to_response(self.get_context_data(form=form , form2=form2))

def crear_entrada(request, plantilla='crear_entradas_m.html'):
    if request.method == 'POST':
        form = Entrada_productoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("entrada_producto")
    else:
        form = Entrada_productoForm()
    return render(request,plantilla, {'form' : form})

def modificar_entrada(request,pk , plantilla="modificar_entrada.html"):
    if request.method =='POST':
        entradas = get_object_or_404(Entrada_producto, pk=pk)
        form = Entrada_productoForm(request.POST or None, instance = entradas )
        if form.is_valid():
            form.save()
            return redirect("entrada_producto")
    else:
        entradas = get_object_or_404(Entrada_producto, pk=pk)
        form = Entrada_productoForm(request.POST or None,instance=entradas)
    return render(request,plantilla,{'form': form})
def eliminar_entrada(request, pk, plantilla="eliminar_entrada.html"):
    if request.method =='POST':
        estado = Entrada_producto.objects.get(pk=pk)
        estado.estado = 0
        entrada = get_object_or_404(Entrada_producto,pk=pk)
        form = Entrada_productoForm(request.POST or None, instance = entrada)
        if form.is_valid():
            estado.save()
            return redirect("entrada_producto")
    else: 
        entrada = get_object_or_404(Entrada_producto, pk=pk)
        form = Entrada_productoForm(request.POST or None,  instance = entrada)
    return render(request,plantilla, {'form':form})

    
class Detalle_facturaUpdateView(UpdateView):
    model = Detalle_factura
    second_model = Cabecera_factura
    template_name = "modificar_factura.html"
    form_class = Detalle_facturaForm
    second_form_class  = Cabecera_facturaForm
    success_url = reverse_lazy('principal_factura')

    def get_context_data(self , **kwargs):
        context = super(Detalle_facturaUpdateView, self) .get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        detalle =self.model.objects.get(id= pk)
        cabecera = self.second_model.objects.get(id = detalle.cabecera_f_id_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2']  = self.second_form_class(instance = cabecera)
        context['id'] =pk
        return context
    def post(self, request,*args, **kwargs):
        self.object = self.get_object
        pk = self.kwargs.get('pk',0)
        id_detalle = pk
        detalle = self.model.objects.get(id=id_detalle)
        cabecera = self.second_model.objects.get(id=detalle.cabecera_f_id_id)
        form = self.form_class(request.POST, instance = detalle)
        form2 = self.second_form_class(request.POST, instance =cabecera)
        if form.is_valid() and form2.is_valid():
            detalles = form.save(commit=False)
            detalles.cabecera_f_id = form2.save()
            detalles.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form , form2=form2))

    

class Detalle_facturaDeleteView(DeleteView):
    model = Cabecera_factura
    template_name = "eliminar_factura.html"
    success_url = reverse_lazy('principal_factura')


class Eliminar_facturaUpdateView(UpdateView):
    model = Detalle_factura
    second_model = Cabecera_factura
    template_name = "modificar_factura.html"
    form_class = Detalle_facturaForm
    second_form_class  = Cabecera_facturaForm
    success_url = reverse_lazy('principal_factura')

    def get_context_data(self , **kwargs):
        context = super(Eliminar_facturaUpdateView, self) .get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        detalle =self.model.objects.get(id= pk)
        cabecera = self.second_model.objects.get(id = detalle.cabecera_f_id_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2']  = self.second_form_class(instance = cabecera)
        context['id'] =pk
        return context
    def post(self, request,*args, **kwargs):
        self.object = self.get_object
        pk = self.kwargs.get('pk',0)
        id_detalle = pk
        estado1 = self.model.objects.get(pk=id_detalle)
        estado1.estado = 0
        estado2 = self.second_model.objects.get(pk=id_detalle)
        estado2.estado = 0
        detalle = self.model.objects.get(id=id_detalle)
        cabecera = self.second_model.objects.get(id=detalle.cabecera_f_id_id)
        form = self.form_class(request.POST, instance = detalle)
        form2 = self.second_form_class(request.POST, instance =cabecera)
        if form.is_valid() and form2.is_valid():
            estado1.save()
            estado2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form , form2=form2))

def crear_salida(request, plantilla='crear_salida.html'):
    if request.method == 'POST':
        form = Salida_productoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("salida_producto")
    else:
        form = Entrada_productoForm()
    return render(request,plantilla, {'form' : form})

def modificar_salida(request,pk , plantilla="modificar_entrada.html"):
    if request.method =='POST':
        salidas = get_object_or_404(Salida_producto, pk=pk)
        form = Salida_productoForm(request.POST or None, instance = salidas )
        if form.is_valid():
            form.save()
            return redirect("salida_producto")
    else:
        salidas = get_object_or_404(Salida_producto, pk=pk)
        form = Salida_productoForm(request.POST or None,instance=salidas)
    return render(request,plantilla,{'form': form})
def eliminar_salida(request, pk, plantilla="eliminar_entrada.html"):
    if request.method =='POST':
        estado = Salida_producto.objects.get(pk=pk)
        estado.estado = 0
        salida = get_object_or_404(Salida_producto,pk=pk)
        form = Salida_productoForm(request.POST or None, instance = salida)
        if form.is_valid():
            estado.save()       
            return redirect("principal_factura")
    else: 
        salida = get_object_or_404(Salida_producto, pk=pk)
        form = Salida_productoForm(request.POST or None,  instance = salida)
    return render(request,plantilla, {'form':form})


def prueba(request,pk,plantilla= "factura_prueba.html"):
    if request.method =='POST':
        estado = Cabecera_factura.objects.get(pk=pk)
        cabeza = get_object_or_404(Cabecera_factura,pk=pk)
        form = Cabecera_facturaForm(request.POST or None, instance = cabeza)
        cabecera_id = Cabecera_factura.objects.get( pk = pk)
        detalles = Detalle_factura.objects.filter( cabecera_f_id = cabecera_id.id )
        if form.is_valid():
            valor2 = Detalle_factura.objects.filter(cabecera_f_id =cabeza )
            x=0  
            for n in valor2:
                x= x+ n.subtotal
            print(x)
            cabecera_id.subtotal = x
            cabecera_id.save()
            return redirect("principal_factura")
      
    else:
        cabeza = get_object_or_404(Cabecera_factura,pk=pk)
        form = Cabecera_facturaForm(request.POST or None, instance = cabeza)
        cabecera_id = Cabecera_factura.objects.get( pk = pk)
        detalles = Detalle_factura.objects.filter( cabecera_f_id = cabeza )
        form = Cabecera_facturaForm(request.POST or None, instance = cabeza)
        valor2 = Detalle_factura.objects.filter(cabecera_f_id=cabeza ) 
        valor3 = Cabecera_factura.objects.filter(pk=pk )   

        return render(request, plantilla, {'form':form, 'form2': detalles,'form3': valor3})
        
    return render(request, plantilla, {'form':form, 'form2': detalles, })


def crear_detalles(request,pk,plantilla='Detalles_de_Factura.html'):
    if request.method == 'POST':
        dato= int(pk)

        form = Detalle_facturaForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            valor = Detalle_factura.objects.filter(cabecera_f_id__isnull=True )
            cabecera_id = Cabecera_factura.objects.get( pk = pk)
            for i in valor:
                print(str(i.precio))
                i.cabecera_f_id_id = dato       
                i.save()
            valor2 = Detalle_factura.objects.filter(cabecera_f_id =pk )
            x=0  
            for n in valor2:
                x= x+ n.subtotal
            print(x)
            cabecera_id.subtotal = x
            cabecera_id.save()

            
            

            return redirect("prueba", pk= pk)
    else:
        form = Detalle_facturaForm()
    return render(request,plantilla, {'form' : form})

