from django.urls import path
from . import views
app_name = "app_med"

urlpatterns = [
    path('inicio/', views.index, name = "inicio"),
]
