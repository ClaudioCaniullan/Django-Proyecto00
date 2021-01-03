
from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('hemograma', views.Hemograma),
    # path('perfilbioquimico', views.PerfilBioquimico),
    # path('perfillipidico', views.PerfilLipidico),
    # path('orina', views.Orina),
    # path('coagulacion', views.Coagulacion),
    # path('glicemia', views.Glicemia),
    # path('electrocardiograma', views.Electrocardiograma),

]