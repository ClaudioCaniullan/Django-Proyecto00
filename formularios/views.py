from django.shortcuts import render, redirect
from .forms import CrearUsuario
from django.conf import settings
import json

# Create your views here.

def crear_usuario1(request):
    mensaje = "HOLA MUNDO"
    data = {'prueba': mensaje}
    return render(request, 'formularios/crear_usuario.html', context=data)

def crear_usuario(request):
    add_user = CrearUsuario(request.POST or None)
    context = {'form', add_user}
    if formulario.is_valid():
###