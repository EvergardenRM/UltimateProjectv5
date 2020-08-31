from django.db import models

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

    class Meta:
        db_table = "cliente"
        verbose_name = "cliente"
        verbose_name_plural = "personas"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "producto"
        verbose_name = "producto"
        verbose_name_plural = "productos"

    


