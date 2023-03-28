from sqlite3 import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from moduloUsuarios.models import User
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate

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

