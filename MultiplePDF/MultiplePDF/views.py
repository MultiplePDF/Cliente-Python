from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def descarga(request):
    return render(request, 'Descarga.html')