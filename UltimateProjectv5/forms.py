from django import forms
from migarations.models import *

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
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
    cedula = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Cedula'}))   
    nombre = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))   
    apellido = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellido'}))   
    edad = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Edad'}))   
    email = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email'}))   
    sexo = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Sexo'}))   

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
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descripcion'}),
            'precio' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Precio'}),
            'marca_id' : forms.Select(attrs={'class':'form-control', 'placeholder': 'Marca'}),

        }

class MarcaForm(forms.ModelForm):
    nombre = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Marca'}), label ="Nombre")   
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
            'codigo_factura' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Numero de Factura'}),
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

class  Entrada_productoForm(forms.ModelForm):
    
    class Meta:
        model =  Entrada_producto
        fields = (
            'Producto_id',
            'descripcion',
            'cantidad',
            'precio',
        
            )
        labels = {
            'Producto_id' : 'Producto',
            'descripcion' : 'Descripcion',
            'cantidad': 'Cantidad',
            'precio': 'Precio',
        }
        widgets = {
            'Producto_id' : forms.Select(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'precio' : forms.TextInput(attrs={'class':'form-control'}),
        }

class Salida_productoForm(forms.ModelForm):
    
    class Meta:
        model = Salida_producto
        fields = ("Producto_id",
                'descripcion',
                'cantidad',
                'precio',
                
        )

        labels = {
            'Producto_id' : 'Producto',
            'descripcion' : 'Descripcion',
            'cantidad' : 'Cantidad' ,
            'precio' : 'Precio',

        }
        widgets = {

            'Pruducto_id' : forms.Select(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidad '  : forms.TextInput(attrs={'class':'form-control'}),
            'precio' :  forms.TextInput(attrs={'class':'form-control'}),


        }


class RolForm(forms.ModelForm):
    
    class Meta:
        model = Rol
        fields = ("nombre",)
        labels = {
            'nombre' : 'Rol',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
        }


class Rol_UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Rol_Usuario
        fields = ("usuario",
            'rol',
        )
        labels = {
            'rol' : 'Rol',
            'usuario' : 'Usuario',
        }
        widgets = {
            'rol' : forms.Select(attrs={'class':'form-control'}),
            'usuario' : forms.Select(attrs={'class':'form-control'}),
        }



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth')
        labels = {
            'username' : 'Username',
            'email' : 'Email',
            'date_of_birth': 'Fecha Nacimiento',
            
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
#admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)