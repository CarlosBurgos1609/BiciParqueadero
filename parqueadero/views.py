from django.shortcuts import render
from django.contrib.auth import logout

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
        # traer usuarios BD y comparar contraseña encriptada
        # if la contraseña y correo son correctos, rendirijes al homne
        # else renderisar el mismo formulario con error de correo o contraseña incorrecta
        return render(request, 'parqueadero/login.html', )

def register(request):
    sedes = Sede.objects.all()
    return render(request, 'parqueadero/register.html',{'sedes':sedes})



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

