from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("admin/", views.admin),
    path("paciente/", views.paciente),
]