from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import usuario

def index(request):
    return HttpResponse(":::Welcom to my site:::")
def lista_usurio(request):
    #return HttpResponse ("Here you find a list of users")
    usuarios = usuario.objects.all()
    return render(request, 'parqueadero/user.html', {'usuario':usuarios})

def login(request):
    #return HttpResponse ("Here you find a list of users")
    return render(request, 'parqueadero/login.html',)

