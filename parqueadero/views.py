from django.db import IntegrityError
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from django.http import HttpResponse
from .models import usuario
from .models import Sede
from .forms import usuariosForm


def index(request):
    return HttpResponse(":::Welcom to my site:::")


def lista_usurio(request):
    # return HttpResponse ("Here you find a list of users")
    usuarios = usuario.objects.all()
    return render(request, 'parqueadero/user.html', {'usuario': usuarios})


def login(request):
    if request.method == "GET":
        print('enviando formulario')

    else:
        print(request.POST)
        print('obteniendo datos')

    return render(request, 'parqueadero/login.html', {
        'form': UserCreationForm

    })
    # else:
    #     # if request.POST['password1'] == request.POST['password2']:
    #     #     usuario = usuario.objects.create_user(username=request.POST['username'],
    #     #                                         password=request.POST['password1'])

    #     #     return HttpResponse('contraseña incorrecta')

    #     print(request.POST)
    #     print('obteniendo datos')

    # elif request.method == "POST":
    #    email = request.POST.get('email')
    #    password = request.POST.get('password')
    #
    #    if email and password:
    #        usuario = authenticate(email=email, password=password)
    #        if usuario is not None:
    #            login(request, usuario)
    #
    #            return redirect('home')
    #        else:
    #
    #            return render(request, 'parqueadero/login.html', {'error_message': 'Correo electrónico o contraseña incorrectos.'})
    #    else:
    #
    #        return render(request, 'parqueadero/login.html', {'error_message': 'Por favor, ingrese correo electrónico y contraseña.'})


def register(request):
    form = usuariosForm()
    if request.method == "POST":
        form = usuariosForm(request.POST)
        if form.is_valid():
            try:
                user = usuario()

                user.nombre = form.cleaned_data['nombre']
                user.apellido = form.cleaned_data['apellido']
                user.código = form.cleaned_data['codigo']
                user.identificación = form.cleaned_data['identificacion']
                user.password = form.cleaned_data['password']
                user.email = form.cleaned_data['email']
                user.id_programas = form.cleaned_data['id_programa']
                user.save()

                return redirect('home')

            except IntegrityError:
                # Manejar el error de integridad (correo electrónico duplicado)
                error_message = "Ya existe un usuario registrado con este correo electrónico."
                return render(request, 'parqueadero/register.html', {'form': form, 'error_message': error_message})

    return render(request, 'parqueadero/register.html', {'form': form})
    # usuario
    # sedes = Sede.objects.all()
    # return render(request, 'parqueadero/register.html', {'sedes': sedes})


# @login_required
def home(request):

    # if estoy logeado me quedo
    # else redirecciono al loginS
    return render(request, 'parqueadero/home.html')


def points(request):
    return render(request, 'parqueadero/puntos.html')


def headquarters(request):
    return render(request, 'parqueadero/sedes.html')


def my_account(request):
    return render(request, 'parqueadero/mi_cuenta.html')
def  base(request):
    return render(request,'parqueadero\base.html')

