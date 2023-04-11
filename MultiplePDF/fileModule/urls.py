from django.urls import path, include

from fileModule import views

urlpatterns = [
    path('Home/', views.uploadFiles, name='homeArchivos'),
    path('DragDrop/', views.drag_and_drop, name='dragDrop'),
    path('Upload/', views.upload_view, name='upload'),
    path('Json/', views.json_view, name='json'),
    path('Json/template/', views.json_template_view, name='json_template'),

]
