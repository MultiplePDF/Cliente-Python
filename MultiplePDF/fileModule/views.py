from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
import base64
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from zeep import Client
import json
from .forms import FileForm
from .models import File



def drag_and_drop(request):
    if not request.session.get('token'):
        # Si el token no está en la sesión, redirigir al usuario al formulario de login
        return redirect('login2')
    else:
        # Si el usuario está autenticado, mostrar la página dragDrop
        return render(request, 'drag_and_drop.html')



def uploadFiles(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            for file in request.FILES.getlist('files1'):

                name = file.name

                content = base64.b64encode(file.read())
                File.objects.create(fileName=name, serializedFile=content)
            files = File.objects.all()
            return render(request, 'files.html', {'files1': files})
        else:
            message = 'Por favor, corrija los errores en el formulario.'
    else:
        form = FileForm()
        message = ''
    files = File.objects.all()
    return render(request, 'UploadFiles.html', {'form': form, 'files1': files, 'message': message})


def upload_view(request):
    client = Client('http://localhost:8080/ws/countries.wsdl')
    access_token = request.session.get('token')
    print("Hay un token ???", access_token)
    if not access_token:
        return redirect('Login2')
    if request.method == 'POST' and request.FILES.getlist('file'):
        files = request.FILES.getlist('file')
        file_data = []
        for i, file in enumerate(files):
            file_data.append({
                'ID': i + 1,
                'NombreDelDocumento': file.name,
                'Contenido': base64.b64encode(file.read()).decode(),
                'Size': round(file.size / 1024, 2),  # convertir a KB y redondear a 2 decimales
            })
        request.session['file_data'] = file_data
        #print(client.service.uploadFiles(access_token,json.dumps(file_data)))
        return JsonResponse({'files': file_data})
    return render(request, 'drag_and_drop.html')

def json_view(request):
    if request.method == 'POST':
        request.session.pop('file_data', None)
        return JsonResponse({'Mensaje': 'Los files1 cargados se eliminaron correctamente.'})
    file_data = request.session.get('file_data', None)
    if file_data is not None:
        return JsonResponse({'files': file_data})
    return JsonResponse({'Error': 'No se encontró ningún archivo cargado.'})

def json_template_view(request):
    file_data = request.session.get('file_data', None)
    if file_data is not None:
        json_data = {'files': file_data}
    else:
        json_data = {'Error': 'No se encontró ningún archivo cargado.'}
    return render(request, 'ShowJson.html', {'json_data': json_data})



