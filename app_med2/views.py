from django.shortcuts import render
import json

def home(request):

    return render(request,'home.html')

def usuario(request):
    #-------------- Lectura de datos del usuario del .json --------------
    # Generar copia de los datos de usuarios
    with open('../proyecto_web/app_med/data/usuarios.json', 'r') as file:
        usuarios=json.load(file)
    #Seleccionar el usuario requerido y extraer los datos asociados
    usuario=usuarios['9999999-9']
    nombre_us=usuario['nombre']+" "+usuario['apellido']
    edad_us=usuario['edad']
    direccion_us=usuario['direccion']

    #datos a entregar al html
    context_us={'nombre_us':nombre_us,'edad_us':edad_us, 'direccion_us':direccion_us}

    return render(request,'usuario.html',context_us)

def user(request):
    
    #usuario= POST if usuario ="admin": vista admin else: vista paciente

    #-------------- Lectura de datos del usuario del .json --------------
    # Generar copia de los datos de usuarios
    with open('../proyecto_web/app_med/data/usuarios.json', 'r') as file:
        usuarios=json.load(file)
    #Seleccionar el usuario requerido y extraer los datos asociados
    usuario=usuarios['9999999-9']
    nombre_us=usuario['nombre']+" "+usuario['apellido']
    edad_us=usuario['edad']
    direccion_us=usuario['direccion']

    

    #-------------- Lectura de datos de pacientes del .json --------------
    # Generar copia de los datos de pacientes
    with open('../proyecto_web/app_med/data/usuarios.json', 'r') as file:
        pacientes=json.load(file)

    #datos a entregar al html
    context_us={'nombre_us':nombre_us,'edad_us':edad_us, 'direccion_us':direccion_us,'pacientes':pacientes}

    return render(request,'app_med/user.html',context_us)
