from django.shortcuts import render

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
    #return HttpResponse ("Here you find a list of users"
    return render(request, 'parqueadero/login.html')

def register(request):
# return HttpResponse ("Here you find a list of users")
    sedes = Sede.objects.all()
    return render(request, 'parqueadero/register.html',{'sedes':sedes})

def home(request):
    #return HttpResponse ("Here you find a list of users"
    return render(request, 'parqueadero/index.html')

def points(request):
    return render(request, 'parqueadero/puntos.html')

def headquarters(request):
    return render(request, 'parqueadero/sedes.html')

def my_account(request):
    return render(request, 'parqueadero/mi_cuenta.html')

