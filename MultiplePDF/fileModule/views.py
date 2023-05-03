import hashlib
from os import path

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
    return render(request, 'upload-files.html', {'form': form, 'files1': files, 'message': message})


def upload_view(request):
    client = Client('http://java.bucaramanga.upb.edu.co/ws/multiplepdf.wsdl')
    access_token = request.session.get('token')
    print("Hay un token ???", access_token)
    if not access_token:
        return redirect('SignIn')
    if request.method == 'POST' and request.FILES.getlist('file'):
        files = request.FILES.getlist('file')
        file_data = []
        for i, file in enumerate(files):
            archivo = file.read()
            file_extension = path.splitext(file.name)[1]
            #content = base64.b64encode().decode()
            sha256 = hashlib.sha256(archivo).hexdigest()

            file_data.append({
                'idFile': i + 1,
                'base64': base64.b64encode(archivo).decode(),
                'fileName': file.name,
                'fileExtension': file_extension,
                'size': round(file.size / 1024, 2),  # convertir a KB y redondear a 2 decimales
                'checksum' : sha256
            })
        #request.session['file_data'] = file_data
        response = client.service.sendBatch(json.dumps(file_data,ensure_ascii=False),access_token)
        print(response)
        linkDownload = response['downloadPath']
        print(linkDownload)
        if response['successful']:
            return render(request, 'downloads.html', {'linkDownload': linkDownload})
        else:
            return JsonResponse({'error': 'Error al enviar el batch'})


    return render(request, 'drag_and_drop.html',)

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
    return render(request, 'show-json.html', {'json_data': json_data})

def myfiles(request):
    access_token = request.session.get('token')
    print("Hay un token ???", access_token)
    if not access_token:
        return redirect('SignIn')
    # Crear una instancia de Zeep para acceder al servidor WSDL
    wsdl_url = 'http://java.bucaramanga.upb.edu.co/ws/multiplepdf.wsdl'
    client = Client(wsdl=wsdl_url)
    # Llamar al método getBatchDetails del servidor WSDL utilizando el token como parámetro
    response = client.service.getBatchDetails(access_token)
    #print(response)
    # Obtener los detalles
    batch_details = response['batchesList']
    batches = json.loads(batch_details)
    #print(batches) #lotes[0]['files'][0]['fileName']
    data_lotes_details = [{'ID_Batch': item['_id'], 'Files': item['files']} for item in batches]
    request.session['data_lotes_details'] = data_lotes_details
    data_lotes = [{'id': i + 1, 'date': batch['createdAt'], 'numberFiles': batch['numberFiles'],
                   'expirationDate': batch['validity'], 'ID_Batch': batch['_id']} for i, batch in enumerate(batches)]
    print(data_lotes)
    print("*************************************")
    print(data_lotes_details)
    #print(data_lotes)

    # Renderizar la plantilla myfiles.html y pasar los detalles del lote de archivos PDF como contexto
    return render(request, 'my-files.html', {'data': json.loads(json.dumps(data_lotes)), 'batches': data_lotes_details})

def upload_view_urls(request):
    client = Client('http://java.bucaramanga.upb.edu.co/ws/multiplepdf.wsdl')
    access_token = request.session.get('token')
    #print("Hay un token ???", access_token)
    if not access_token:
        return redirect('SignIn')
    if request.method == 'POST':
        urls = request.POST.get('urls')
        urls = urls.strip() # Elimina espacios en blanco al inicio y final
        urls = urls.replace('\n', '') # Elimina saltos de línea
        urls = urls.replace('\r', '')  # Elimina espacios
        urls = urls.split(',') # Convierte en una lista separada por comas
        file_data_urls = []
        for i, url in enumerate(urls):
            file_data_urls.append({
                'idFile': i + 1,
                'base64': url.strip(),
                'fileName': "",
                'fileExtension': "URL",
                'size': 1,
                'checksum': ""
            })

        response = client.service.sendBatch(json.dumps(file_data_urls, ensure_ascii=False), access_token)
        #print(response)
        linkDownload = response['downloadPath']
        #print(linkDownload)
        if response['successful']:
            return render(request, 'downloads.html', {'linkDownload': linkDownload})
        else:
            return JsonResponse({'error': 'Error al enviar el batch'})
    else:
        return HttpResponse('Método no permitido')


def batch_details(request, id_batch):
    # Obtener los detalles del lote de la sesión
    data_lotes_details = request.session.get('data_lotes_details')
    # Buscar el lote con el ID especificado
    batch = next((item for item in data_lotes_details if item['ID_Batch'] == id_batch), None)
    if batch:
        # Si se encontró el lote, obtener los archivos y pasarlos como contexto a la plantilla
        files = batch['Files']
        return render(request, 'my-files-details.html', {'files': files})
    else:
        # Si no se encontró el lote, mostrar un mensaje de error
        message = f"No se encontró ningún lote con el ID {id_batch}."
        return render(request, 'my-files-details.html', {'message': message})





