from django.urls import path, include
from moduloUsuarios import views

urlpatterns = [
    path('registro', views.registro, name='Registro'),
    path('login', views.login, name='Login'),
    path('login2', views.loginMPDF, name='Login2'),
    path('registro2', views.registerMPDF, name='Registro2')

]
