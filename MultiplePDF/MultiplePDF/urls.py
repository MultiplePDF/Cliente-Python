
from django.contrib import admin
from django.urls import path, include

from MultiplePDF import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/descargas', views.descarga, name='descargas'),
    path('myapp/', include('moduloArchivos.urls'))
]
