
from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('tabla_examenes', views.tabla_examenes),
    path('tabla_creada', views.tabla_creada),
    # path('crear_guitarra_manual', views.crear_guitarra_manual),
    path('<id>/borrar', views.eliminar_examen),
]