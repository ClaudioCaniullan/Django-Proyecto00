from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('crear_usuario', views.crear_usuario, name = "crear_usuario"),
    path('usuario_creado', views.usuario_creado, name = "usuario_creado"),
    path('contacto', views.contacto, name = "contacto"),
    path('mensaje_enviado', views.mensaje_enviado, name = "mensaje_enviado")
]
