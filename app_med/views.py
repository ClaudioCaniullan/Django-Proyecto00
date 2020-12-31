from django.shortcuts import render

# Create your views here.

# esta funciòn renderiza index2 que usa como base a index
def mostrar_app_med(request):
    # lista para la cabecera
    list1 = ['Inicio', 'Noticias', 'Nuestro Equipo', 'Informacion', 'Contacto']
    # lista para competencias
    list1_header = [{'Informacion Covid', 'Custodia del Plebicito', 'Covid en Mall Zofri', 'Nuevo control Ingreso' ]
    list1_title = ['Minsal informa 52 fallecidos','Custodia Policiales & Militar', 'Caso positivo en Mall Zofri', 'Ingreso a la R. de los lagos']
    list1_text = ['Laboratorios informaron 37 mil examenes de PCR, 52 Fallecidos y 1773 Nuevos casos activos',
                 'Mas de 50 mil funcionarios Policiales y Militares Custodiaran Plebicito',
                 'Trabajadora del Mall Zofri es Positivo para COVID, ahora esta en cuarentena',
                 'Evaluan nuevo control de ingreso para el sector de Cocule, que se instala el día de hoy']
    
    list2_header = []
    list2_title = []
    list2_text = []

    numeros_a = ['1', '2', '3', '4']
    numeros_b = ['5','6','7']
    enlaces1 = ['1','2']
    enlaces2 = ['3','4']
    datos = {'list1': list1, 'list1_header': list1_header, 'list1_title': list1_title , 'numeros_a': numeros_a, 'numeros_b': numeros_b,
            'enlaces1': enlaces1, 'enlaces2': enlaces2}
    return render(request, 'app_med/base.html', context=datos)