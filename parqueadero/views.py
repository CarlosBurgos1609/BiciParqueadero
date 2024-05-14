from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.
from django.http import HttpResponse
from .models import usuario, Punto

from .forms import inicioForm, usuariosForm


def index(request):
    return HttpResponse(":::Welcom to my site:::")


def lista_usurio(request):
    # return HttpResponse ("Here you find a list of users")
    usuarios = usuario.objects.all()
    return render(request, 'parqueadero/user.html', {'usuario': usuarios})


def loguin(request):
    form = inicioForm()
    if request.method == "POST":
        form = inicioForm(request.POST)
        if form.is_valid():
            try:
                user = authenticate(
                    request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if user is None:
                    print('hola login')
                    error_message = "correo o contraseña incorrectos."
                    return render(request, 'parqueadero/login.html', {'form': form, 'error_message': error_message})

                login(request, user)

                return redirect('home')

            except IntegrityError:
                print('lola')
                error_message = "correo o contraseña incorrectos."
                return render(request, 'parqueadero/login.html', {'form': form, 'error_message': error_message})

    return render(request, 'parqueadero/login.html', {'form': form})


def register(request):
    form = usuariosForm()
    if request.method == "POST":
        form = usuariosForm(request.POST)
        if form.is_valid():
            # form.cleaned_data['password']
            try:
                usuario_nuevo = usuario()

                usuario_nuevo.nombre = form.cleaned_data['nombre']
                usuario_nuevo.apellido = form.cleaned_data['apellido']
                usuario_nuevo.código = form.cleaned_data['codigo']
                usuario_nuevo.identificación = form.cleaned_data['identificacion']
                usuario_nuevo.password = form.cleaned_data['password']
                usuario_nuevo.email = form.cleaned_data['email']
                usuario_nuevo.id_programas = form.cleaned_data['id_programa']

                usuario_nuevo.save()
                user = User.objects.create_user(
                    form.cleaned_data['email'], password=form.cleaned_data['password'])
                user.save()
                login(request, user)               

                return redirect('home')

            except IntegrityError:

                error_message = "Ya existe un usuario registrado con este correo electrónico."
                return render(request, 'parqueadero/register.html', {'form': form, 'error_message': error_message})

    return render(request, 'parqueadero/register.html', {'form': form})


def home(request):

    return render(request, 'parqueadero/home.html')

    # if estoy logeado me quedo
    # else redirecciono al loginS


def points(request):
    puntos = Punto.objects.all()
    return render(request, 'parqueadero/puntos.html', {'Punto': puntos})


def headquarters(request):
    return render(request, 'parqueadero/sedes.html')


@login_required
def my_account(request):
    user = usuario.objects.get(email__exact=request.user.username)

    return render(request, 'parqueadero/mi_cuenta.html', {'usuario': user})


def base(request):
    return render(request, 'parqueadero\base.html')


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')
