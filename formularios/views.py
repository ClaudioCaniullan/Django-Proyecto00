from django.shortcuts import render, redirect
from .forms import Hemograma
from django.conf import settings
import json
# Create your views here.


def hemograma(request):
    formulario = hemograma(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        filename = "/formularios/static/formularios/data/examenes.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            examenes = json.load(file)
        examenes['examenes'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, "w") as file:
            json.dump(examenes, file)
        # return redirect('formularios:tabla_creada')
    return render(request, 'formularios/hemograma.html', context)


