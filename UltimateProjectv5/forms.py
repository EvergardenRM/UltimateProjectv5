from django import forms
from migarations.models import Cliente, Producto
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
    class Meta:
        model = Cliente
        fields=['cedula','nombre', 'apellido', 'edad','email','sexo']
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion','precio')
