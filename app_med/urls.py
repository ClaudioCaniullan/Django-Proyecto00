from django.urls import path
from . import views

urlpatterns = [
    path('app_med/', views.mostrar_app_med ),
]
