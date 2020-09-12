from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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

