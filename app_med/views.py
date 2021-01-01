from django.shortcuts import render

# Create your views here.

# esta funciòn renderiza index2 que usa como base a index
def mostrar_app_med(request):
    # lista para la cabecera
    list1 = ['Inicio', 'Noticias', 'Nuestro Equipo', 'Informacion', 'Contacto']
    datos = {'list1': list1, }
    return render(request, 'app_med/00.html', context=datos)