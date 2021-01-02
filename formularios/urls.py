
from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('tabla_examenes', views.tabla_examenes),
    path('tabla_creada', views.tabla_creada),
    path('<id>/borrar', views.eliminar_examen),
]