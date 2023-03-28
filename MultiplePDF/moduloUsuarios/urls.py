from django.urls import path, include
from moduloUsuarios import views

urlpatterns = [
    path('Usuarios/registro', views.signup, name='Registro'),
    path('Usuarios/login', views.login, name='Login')
]
