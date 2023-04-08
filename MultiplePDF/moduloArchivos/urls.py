from django.urls import path, include

from moduloArchivos import views

urlpatterns = [
    path('Home/', views.subir_archivos, name='homeArchivos'),
    path('DragDrop/', views.drag_and_drop, name='dragDrop')
]
