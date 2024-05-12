from django import forms
from .models import Programa

class usuariosForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=150, required=True)
    apellido = forms.CharField(label="apellido",max_length=150, required=True)
    codigo = forms.CharField(label="codigo",max_length=11, required=True)
    identificacion = forms.CharField(label="identificacion",max_length=11, required=True)
    email = forms.CharField(label="email",max_length=200, required=True)
    password =forms.CharField(label="contraseña",max_length=250, required=True)
    id_programa = forms.ModelChoiceField(label="programa", queryset= Programa.objects.all()) 
    
    
    