from django.urls import path, include
from userModule import views

urlpatterns = [
    path('registro', views.registro, name='Registro'),
    path('login', views.login, name='Login'),
    path('SignIn', views.loginMPDF, name='SignIn'),
    path('SignUp', views.registerMPDF, name='SignUp')

]
