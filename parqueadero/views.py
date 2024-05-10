from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from .models import usuario
from .models import Sede

def index(request):
    return HttpResponse(":::Welcom to my site:::")
def lista_usurio(request):
    #return HttpResponse ("Here you find a list of users")
    usuarios = usuario.objects.all()
    return render(request, 'parqueadero/user.html', {'usuario':usuarios})

def login(request):
    if request.method == "GET":
        return render(request, 'parqueadero/login.html')
    elif request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        usuario = authenticate(email=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            return render(request, 'parqueadero/login.html')

def register(request):
    sedes = Sede.objects.all()
    return render(request, 'parqueadero/register.html',{'sedes':sedes})


@login_required
def home(request):
    # if estoy logeado me quedo
    # else redirecciono al loginS 
    return render(request, 'parqueadero/index.html')

def points(request):
    return render(request, 'parqueadero/puntos.html')

def headquarters(request):
    return render(request, 'parqueadero/sedes.html')

def my_account(request):
    return render(request, 'parqueadero/mi_cuenta.html')

