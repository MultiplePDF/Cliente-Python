from django.urls import path, include
from moduloUsuarios import views

urlpatterns = [
    path('Usuarios/registro', views.registro, name='Registro'),
    path('Usuarios/login', views.login, name='Login')
]
