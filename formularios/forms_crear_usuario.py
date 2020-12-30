from django import forms

class CrearUsuario(forms.Form):
    nombre = forms.CharField()
    edad =  forms.IntegerField()
    direccion = forms.CharField()
    tipo_usuario = forms.CharField()
    fecha_creacion = forms.DateField()
