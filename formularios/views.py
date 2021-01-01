from django.shortcuts import render, redirect
from .forms import DiagnosticoExamen
from django.conf import settings
import json
# Create your views here.


def tabla_examenes(request):
    formulario = DiagnosticoExamen(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        filename = "/formularios/static/formularios/data/examenes.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            examenes = json.load(file)
        examenes['examenes'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, "w") as file:
            json.dump(examenes, file)
        return redirect('formularios:tabla_creada')
    return render(request, 'formularios/tabla_examenes.html', context)


def tabla_creada(request):
    filename= "/formularios/static/formularios/data/examenes.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        examenes=json.load(file)
    return render(request, 'formularios/tabla_creada.html', context=examenes)

def eliminar_examen(request, id):
    if request.method == "POST":
        filename= "/formularios/static/formularios/data/examenes.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            examenes=json.load(file)
        for examen in examenes['examenes']:
            print(int(examen['id']), int(id))
            if int(examen['id']) == int(id):
                guitarras['examenes'].remove(examen)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(examenes, file)
        return redirect('formularios:tabla_creada')
    context = {'id': id} 
    return render(request, "formularios/eliminar_examen.html", context) 