from django.urls import path, include

from moduloArchivos import views

urlpatterns = [
    path('Archivos/', views.subir_archivos, name='homeArchivos'),
]
