
from django.contrib import admin
from django.urls import path, include

from MultiplePDF import views

urlpatterns = [
<<<<<<< HEAD
    path('Home', views.home, name='home'),
    path('Descargas', views.descarga, name='descargas'),
    path('Archivos/', include('moduloArchivos.urls')),
    path('Usuarios/', include('moduloUsuarios.urls')),
=======
    path('', views.home, name='home'),
    path('/descargas', views.descarga, name='descargas'),
    path('Archivos/', include('fileModule.urls')),
    path('Usuarios/', include('userModule.urls')),
>>>>>>> 80d0bdfe0858e58007c6aa578ba57f579d39ba3e
    path('calculator/', views.calculate, name='calculadora')
]
