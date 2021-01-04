
from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('hemograma', views.hemograma, name='hemograma'),
    path('perfilbioquimico', views.perfil_bioquimico, name='perfil_bioquimico'),
    path('perfillipidico', views.perfil_lipidico, name='perfil_lipidico'),
    path('orina', views.orina, name='orina'),
    path('coagulacion', views.coagulacion, name='coagulacion'),
    path('glicemia', views.glicemia, name='glicemia'),
    path('electrocardiograma', views.electro_cardiograma, name='electro_cardiograma'),
    path('formularioOK', views.formularioOK, name='formularioOK'),

]