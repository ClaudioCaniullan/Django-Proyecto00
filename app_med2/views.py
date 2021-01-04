from django.shortcuts import render
import json

#Table
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

def home(request):

    return render(request,'home.html')

def admin(request):

    #-------------- Lectura de datos del usuario del .json --------------
    # Generar copia de los datos de usuarios
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        usuarios=json.load(file)
    #Seleccionar el usuario requerido y extraer los datos asociados
    usuario=usuarios['9999999-9']
    nombre_us=usuario['nombre']+" "+usuario['apellido']
    edad_us=usuario['edad']
    direccion_us=usuario['direccion']

    #-------------- Lectura de datos de pacientes del .json --------------
    # Generar copia de los datos de pacientes
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        pacientes=json.load(file)

    lpacientes=pacientes

    #datos a entregar al html
    context_us={'nombre_us':nombre_us,'edad_us':edad_us, 'direccion_us':direccion_us,'lpacientes':lpacientes}

    return render(request,'admin.html',context_us)

def paciente(request):
    return render(request,'paciente.html')
