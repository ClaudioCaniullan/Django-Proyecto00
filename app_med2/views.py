from django.shortcuts import render
import json

#Forms
from .forms_crear_usuario import CrearUsuario, Contacto

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

    #-------------- Creación de usuario por formulario --------------
    add_user = CrearUsuario(request.POST or None)
    
    if add_user.is_valid():
        form_data = add_user.cleaned_data
        #form_data['fecha_creacion']=form_data['fecha_creacion'].strftime("%Y-%m-%d")
        
        #usuarios.append(form_data)
        with open('../proyecto_web/app_med2/data/usuarios.json', 'w') as file:
            json.dump(usuarios, file)
        #return redirect('formularios:usuario_creado')
    

    #datos a entregar al html
    context_us={'nombre_us':nombre_us,'edad_us':edad_us, 'direccion_us':direccion_us,'lpacientes':lpacientes,'form_pac': add_user}

    return render(request,'admin.html',context_us)

def paciente(request):

    #Vista usuario por defecto --> primero del listado
    # Generar copia de los datos de usuarios
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        pacientes=json.load(file)

    #Extraer ruts para lista desplegable de cambio de usuario
    rut_pacs=[]
    for p in pacientes:
        rut_pacs.append(p)
        break

    #Extraer primer rut
    f_pac=rut_pacs[0]
    # Extracción datos del paciente
    data_pac= pacientes[f_pac]

    # --------------------- Datos de vista por defecto --------------------- 
    #Datos paciente
    rut_pac=data_pac['rut']
    nombre_pac=data_pac['nombre']+" "+data_pac['apellido']
    edad_pac=data_pac['edad']
    direccion_pac=data_pac['direccion'] 
    #Examenes
    #Gráficos
    #Formulario Exámenes



    #Datos a entregar al html
    context_pac={'nombre_us':nombre_pac,'edad_us':edad_pac, 'direccion_us':direccion_pac,'rut_pacs':rut_pacs}
    return render(request,'paciente.html',context_pac)
