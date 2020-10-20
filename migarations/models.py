from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core import validators
from django.core.validators import RegexValidator, validate_email
from django.urls import reverse
# Create your models here.
from django.contrib import admin 
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    username = models.CharField(('username'), max_length=200, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[a-z0-9_-]*$',
            message='Usernames can only contain letters, numbers, underscores, and dashes.'
        )
    ])
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[validators.validate_email]
    )

    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','date_of_birth']

    def __str__(self):
        return '{}'.format(self.username)


    def get_absolute_url(self):
        return reverse('modificar_usuario', kwargs={'pk': self.pk})

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class project(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField()
    genero = models.CharField(max_length=2)
    estado = models.IntegerField()
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "persona"
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ['created']

    def __str__(self):
        return self.apellido + ' ' + self.nombre
class Cliente(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    edad = models.IntegerField()
    sexo = models.CharField(max_length=20)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "cliente"
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
    def __str__(self):
        return '{}'.format(self.apellido+' '+self.nombre)
    
    

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    f_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)
    class Meta:
        db_table = "marca"
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    def __str__(self):
        return '{}'.format(self.nombre)
    

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    marca_id = models.ForeignKey(Marca, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "producto"
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["descripcion"]
    def __str__(self):
        return '{}'.format(self.nombre)

class Cabecera_factura(models.Model):
    codigo_factura = models.CharField( max_length=15)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    f_emision = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.DecimalField( max_digits=10, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField( max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField( max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "cabecera_factura"
        verbose_name = "cabecera_factura"
        verbose_name_plural = "cabecera_facturas"
    def __str__(self):
        return self.codigo_factura
    def save(self):
        if self.subtotal:
            self.iva = float(self.subtotal) * float(0.12)
            self.total = float(self.subtotal) + float(self.iva)
            super(Cabecera_factura, self).save() 
        else:
            super(Cabecera_factura, self).save() 

    

class Detalle_factura(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cabecera_f_id = models.ForeignKey(Cabecera_factura, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField( max_digits=10, decimal_places=2)
    total_pagar = models.DecimalField( max_digits=10, decimal_places=2)
    f_emision = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)
    class Meta:
        db_table = "detalle_factura"
        verbose_name = "detalle_factura"
        verbose_name_plural = "detalle_facturas"
    def __str__(self):
        return self.id
    def save(self):
        self.subtotal = float(float(int(self.cantidad))) * float(self.precio)
        self.iva = float(self.subtotal) * float(0.12)
        self.total_pagar = self.subtotal + self.iva
        super(Detalle_factura, self).save()
        
    
class Entrada_producto(models.Model):
    Producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.CharField( max_length=100)
    precio = models.DecimalField( max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    f_creacion = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField( max_digits=10, decimal_places=2)
    estado = models.IntegerField(default=1)
    class Meta:
        db_table = "entrada_producto"
        verbose_name = "entrada_producto"
        verbose_name_plural = "entrada_productos" 
    def __str__(self):
        return self.descripcion
    
    def save(self):
        self.monto = float(float(int(self.cantidad))) * float(self.precio)
        super(Entrada_producto, self).save()
    

class Salida_producto(models.Model):
    Producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.CharField( max_length=100)
    precio = models.DecimalField( max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    monto = models.DecimalField( max_digits=10, decimal_places=2)
    f_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default =1)
    class Meta:
        db_table = "salida_producto"
        verbose_name = "salida_producto"
        verbose_name_plural = "salida_productos"
    def __str__(self):
        return self.descripcion
    def save(self):
        if self.subtotal:
            self.monto = float(float(int(self.cantidad))) * float(self.precio)
            super(Salida_producto,  self).save()


class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField(default=1)
    class Meta:
        db_table = "rol"
        verbose_name = "Rol"
        verbose_name_plural = "Rols"
        ordering = ('nombre',)


    def __str__(self):
        return '{}'.format(self.nombre)

class Rol_Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.IntegerField(default =1)
    class Meta:
        db_table = "rolusuario"
        verbose_name = "rolusuario"
        verbose_name_plural = "rolusuarios"
    def __str__(self):
        return self.rol_id, 


    

    

    
