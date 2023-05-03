from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from zeep import Client

def home(request):
    return render(request, 'home.html')

def descarga(request):
    return render(request, 'download.html')

def calculate(request):
    result = None

    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))

        wsdl = 'http://www.dneonline.com/calculator.asmx?wsdl'
        client = Client(wsdl)

        result = client.service.Add(number1, number2)

    return render(request, 'calculator.html', {'result': result})

