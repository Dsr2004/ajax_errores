from django.db import models

# Create your models here.

class frutas(models.Model):
    id_fruta=models.AutoField("Id de la Fruta", primary_key=True, unique=True)
    nombre=models.CharField("Nombre", max_length=40, null=False, blank=False, unique=True)
    descripcion=models.TextField("Descripcion",null=False,blank=False)
    precio=models.IntegerField("Precio",null=False, blank=False)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)