from django import forms
from migarations.models import *
from django.contrib.auth.models import User
class RegisterForm(forms.Form):
    username = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'id': 'username'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'id':'email'}))
    password = forms.CharField(required=True, max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar Password', required=True, max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra registrado')
        return username

    def clean(self): # para comparar dos attributos de la misma clase.
        cleaned_data = super().clean() #obtener informacion  de la contraseña el super().
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'el password no coincide')

class ClienteForm(forms.ModelForm):
    cedula = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))   
    nombre = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))   
    apellido = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))   
    edad = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))   
    email = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))   
    sexo = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))   

    class Meta:
        model = Cliente
        fields=[
            'cedula',
            'nombre',
            'apellido',
            'edad',
            'email',
            'sexo'
            ]
        labels = {
            'nombre': 'Nombre',
            'cedula': 'Cedula',
            'Apellido': 'Apellido',
            'Edad': 'Edad',
            'Email': 'Email',
            'Sexo': 'Sexo',
            

        }
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre',
         'descripcion',
         'precio',
         'marca_id'

         ]
        labels = {
            'nombre' : 'Nombre',
            'descripcion': 'Descripcion',
            'precio' : 'Precio',
            'marca_id' : 'marca',
        
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'precio' : forms.TextInput(attrs={'class':'form-control'}),
            'marca_id' : forms.Select(attrs={'class':'form-control'}),

        }

class MarcaForm(forms.ModelForm):
    nombre = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}), label ="Nombre")   
    class Meta:
        model = Marca
        fields =("nombre",)
class Cabecera_facturaForm(forms.ModelForm):
    
    class Meta:
        model = Cabecera_factura
        fields = (
            "codigo_factura",
            'cliente_id',
            'user_id',
            
             
        )
        labels = {
            'codigo_factura' : 'No_Factura',
            'cliente_id' : 'Cliente',
            'user_id' : 'User',
            
            
        }
        widgets = {
            'codigo_factura' : forms.TextInput(attrs={'class':'form-control'}),
            'cliente_id' : forms.Select(attrs={'class':'form-control'}),
            'user_id' : forms.Select(attrs={'class':'form-control'}),
            
        }

class Detalle_facturaForm(forms.ModelForm):
    
    class Meta:
        model = Detalle_factura
        fields = (
            'producto_id',
            'cantidad',
            'precio',
                   
            

        )

        labels = {
            'producto_id': 'Producto',
            'cantidad': 'Cantidad',
            'precio' : 'Precio',
            
            
        }
        widgets ={
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'subtotal': forms.TextInput(attrs={'class':'form-control'}),
            'producto_id': forms.Select(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            
        }
