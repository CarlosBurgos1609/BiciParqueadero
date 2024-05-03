from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True
        
class Usuario(DateTimeModel):
    id_usuario= models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    código = models.CharField(max_length=50, blank=False, null=False)
    identificación = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    contrasena = models.CharField(max_length=50, blank=False, null=False)
    estado = models.BooleanField(default=True)
    #jave foranea de programa 
    id_programas = models.ForeignKey(Programa, on_delete=models.CASCADE, blank=False, null=False)

class Programa(DateTimeModel):
    id_programa = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    abrebiación = models.CharField(max_length=5, blank=False, null=False)
    #id _facultad

class Facultade(DateTimeModel):
    id_facultad = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    abrebiación = models.CharField(max_length=5, blank=False, null=False)
    estado = models.BooleanField(default=True)

class Parkine(DateTimeModel):
    id_parking = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    #id usuario
    #id punto
    
class Estacione(DateTimeModel):
    id_estación = models.AutoField(primary_key=True, unique= True, blank= False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    #id sede
    
class Punto(DateTimeModel):
    id_punto = models.AutoField(primary_key=True, unique= True, blank= False, null=False)
    #id_estacion
    estado = models.BooleanField(default=True)
    codigo_punto = models.AutoField(primary_key=True, unique= True, blank= False, null=False)
    
class Sede(DateTimeModel):
    id_sede = models.AutoField(primary_key=True, unique= True, blank= False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    dirección = models.CharField(max_length= 50, blank=False, null=False)