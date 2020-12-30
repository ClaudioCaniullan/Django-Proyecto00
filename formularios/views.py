from django.shortcuts import render, redirect
from .forms_crear_usuario import CrearUsuario
from django.conf import settings
import json

# Create your views here.

def crear_usuario(request):
    add_user = CrearUsuario(request.POST or None)
    context = {'form': add_user}
    if add_user.is_valid():
        form_data = add_user.cleaned_data
        form_data['fecha_creacion']=form_data['fecha_creacion'].strftime("%Y-%m-%d")
        filename= "/formularios/static/formularios/data/usuarios.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:    
            usuarios=json.load(file)
        usuarios['usuarios'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(usuarios, file)
        return redirect('formularios:usuario_creado')
    return render(request, 'formularios/crear_usuario.html', context)

def usuario_creado(request):
    filename= "/formularios/static/formularios/data/usuarios.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        usuarios=json.load(file)
    return render(request, 'formularios/usuario_creado.html', context =usuarios)
