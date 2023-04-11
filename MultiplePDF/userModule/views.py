from sqlite3 import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from userModule.models import User
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from zeep import Client

# Create your views here.

"""def signup (request):
    if request.method=='GET':
        
        user=request.POST['user']
        name_user = request.POST['name_user']
        email = request.POST['email']
        password = request.POST['password']
        u=User.objects.create(user=user, name_user=name_user,password=password,email=email)
        #usuario = User.objects.all()
        u.save()
        #messages.success(request,'El usuario'+request.POST['user'])+'se registró exitosamente')
        HttpResponse("El usuario se registró correctamente")
        return redirect({'% url Login %'})
"""
def signup(request):
    if request.method == 'GET':
        return render(request, 'registrate.html', {"form": SignUpForm})
    else:
        try:
            user = User.objects.create(user=request.POST['user'], name_user=request.POST['name_user'],
                                       password=request.POST['password'], email=request.POST['email'])
            user.save()
            login(request, user)
            return redirect('Login')
        except IntegrityError:
            return render(request, 'registrate.html', {"form": SignUpForm, "error": "Username already exists."})

        return render(request, 'registrate.html', {"form": SignUpForm, "error": "Passwords did not match."})


"""class SignUpView(CreateView):
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('user')
        password = form.cleaned_data.get('password')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')"""
def login(request):
    return render(request, 'login.html')
def registro(request):
    return render(request, 'registrate.html')

from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login
from zeep import Client
from zeep.exceptions import Fault
from django.contrib import messages
from .forms import RegisterForm

def registerMPDF(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        if password != repeat_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect(reverse('Registro2'))

        try:
            client = Client('http://ejemplo.com/mi_wsdl')
            response = client.service.signUp(name, email, password)

            if response == 'success':
                messages.success(request, 'Registro exitoso')
                return redirect(reverse('login2'))
            else:
                messages.error(request, 'Error en el registro')
                return redirect(reverse('signup'))

        except Fault as e:
            messages.error(request, 'Error en el servidor: {}'.format(e.message))
            return redirect('SignUp.html')

    return render(request, 'SignUp.html')

def loginMPDF(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Llamada al servicio web para autenticar al usuario
        client = Client('http://localhost:8080/ws/countries.wsdl')
        token = client.service.login(email, password)
        print("token???", token)

        if token:
            # Si la autenticación es exitosa, guardar el token en la sesión
            request.session['token'] = token
            return redirect('upload')
        else:
            # Si la autenticación falla, mostrar un mensaje de error en el formulario
            error_message = 'Correo electrónico o contraseña incorrectos'
            return render(request, 'SignIn.html', {'error_message': error_message})
    else:
        return render(request, 'SignIn.html')

def logout_view(request):
    if 'token' in request.session:
        del request.session['token']
    return redirect('home')

