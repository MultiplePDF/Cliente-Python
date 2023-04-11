from django.urls import path, include

from fileModule import views

urlpatterns = [
<<<<<<< HEAD:MultiplePDF/moduloArchivos/urls.py
    path('Home/', views.subir_archivos, name='homeArchivos'),
=======
    path('Home/', views.uploadFiles, name='homeArchivos'),
    path('DragDrop/', views.drag_and_drop, name='dragDrop'),
>>>>>>> 80d0bdfe0858e58007c6aa578ba57f579d39ba3e:MultiplePDF/fileModule/urls.py
    path('Upload/', views.upload_view, name='upload'),
    path('Json/', views.json_view, name='json'),
    path('Json/template/', views.json_template_view, name='json_template'),

]
