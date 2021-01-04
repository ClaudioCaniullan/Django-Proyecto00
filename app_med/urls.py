from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index),
    path("user/", views.users),
    path("index2/", views.index2),
]
