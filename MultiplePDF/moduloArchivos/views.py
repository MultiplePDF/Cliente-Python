from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import base64
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import ArchivoForm
from .models import Archivo


def drag_and_drop(request):
    if not request.session.get('token'):
        # Si el token no está en la sesión, redirigir al usuario al formulario de login
        return redirect('login')
    else:
        # Si el usuario está autenticado, mostrar la página dragDrop
        return render(request, 'drag_and_drop.html')



def subir_archivos(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            for archivo in request.FILES.getlist('archivos'):
                nombre = archivo.name
                contenido = base64.b64encode(archivo.read())
                Archivo.objects.create(nombre=nombre, archivo_serializado=contenido)
            archivos = Archivo.objects.all()
            return render(request, 'archivos.html', {'archivos': archivos})
        else:
            mensaje = 'Por favor, corrija los errores en el formulario.'
    else:
        form = ArchivoForm()
        mensaje = ''
    archivos = Archivo.objects.all()
    return render(request, 'subirArchivos.html', {'form': form, 'archivos': archivos, 'mensaje': mensaje})
