
from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('hemograma', views.hemograma),
    path('perfilbioquimico', views.perfil_bioquimico),
    path('perfillipidico', views.perfil_lipidico),
    path('orina', views.orina),
    path('coagulacion', views.coagulacion),
    path('glicemia', views.glicemia),
    path('electrocardiograma', views.electro_cardiograma),

]