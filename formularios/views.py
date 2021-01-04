from django.shortcuts import render, redirect
from .forms import Hemograma, Coagulacion, Electrocardiograma, Glicemia, Orina, PerfilBioquimico, PerfilLipidico
from django.conf import settings
import json
# Create your views here.


def hemograma(request):
    formulario = Hemograma(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        from_data = formulario.cleaned_data
        check_rut = from_data['rut']
        ruta_examenes = "/formularios/static/formularios/data/examenes.json"
        with open(str(settings.BASE_DIR)+ruta_examenes, 'r') as file:
            examenes = json.load(file)
            
    return render(request, 'formularios/hemograma.html', context)


def perfil_bioquimico(request):
    formulario = PerfilBioquimico(request.POST or None)
    context = {'form': formulario}
    return render(request, 'formularios/perfil_bioquimico.html', context)

def perfil_lipidico(request):
    formulario = PerfilLipidico(request.POST or None)
    context = {'form': formulario}
    return render(request, 'formularios/perfil_lipidico.html', context)

def orina(request):
    formulario = Orina(request.POST or None)
    context = {'form': formulario}
    return render(request, 'formularios/orina.html', context)

def coagulacion(request):
    formulario = Coagulacion(request.POST or None)
    context = {'form': formulario}
    return render(request, 'formularios/coagulacion.html', context)

def glicemia(request):
    formulario = Glicemia(request.POST or None)
    context = {'form': formulario}
    return render(request, 'formularios/glicemia.html', context)

def electro_cardiograma(request):
    formulario = Electrocardiograma(request.POST or None)
    context = {'form': formulario}
    return render(request, 'formularios/electro_cardiograma.html', context)

