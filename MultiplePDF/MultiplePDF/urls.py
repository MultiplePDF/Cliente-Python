
from django.contrib import admin
from django.urls import path, include

from MultiplePDF import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/descargas', views.descarga, name='descargas'),
    path('Archivos/', include('moduloArchivos.urls')),
    path('Usuarios/', include('moduloUsuarios.urls')),
    path('calculator/', views.calculate, name='calculadora')
]
