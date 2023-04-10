from django.http import HttpResponse, JsonResponse
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
        return redirect('login2')
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

def upload_view(request):
    if request.method == 'POST' and request.FILES.getlist('file'):
        files = request.FILES.getlist('file')
        file_data = []
        for i, file in enumerate(files):
            file_data.append({
                'ID': i + 1,
                'NombreDelDocumento': file.name,
                'Contenido': base64.b64encode(file.read()).decode(),
                'Size': file.size, #KB
            })
        request.session['file_data'] = file_data
        return JsonResponse({'files': file_data})
    return render(request, 'drag_and_drop.html')

def json_view(request):
    if request.method == 'POST':
        request.session.pop('file_data', None)
        return JsonResponse({'message': 'Los archivos cargados se eliminaron correctamente.'})
    file_data = request.session.get('file_data', None)
    if file_data is not None:
        return JsonResponse({'files': file_data})
    return JsonResponse({'error': 'No se encontró ningún archivo cargado.'})

def json_template_view(request):
    file_data = request.session.get('file_data', None)
    if file_data is not None:
        json_data = {'files': file_data}
    else:
        json_data = {'error': 'No se encontró ningún archivo cargado.'}
    return render(request, 'MostrarJson.html', {'json_data': json_data})

