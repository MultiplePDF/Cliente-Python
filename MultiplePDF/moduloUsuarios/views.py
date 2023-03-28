from django.contrib.auth import authenticate
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView

from moduloUsuarios.models import User
from .forms import SignUpForm


# Create your views here.

def signup (request):
    if request.method=='POST':
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




class SignUpView(CreateView):
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
        return redirect('/')
def login(request):
    return render(request, 'login.html')
def registro(request):
    return render(request, 'registrate.html')

