from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("usuario",views.lista_usurio, name='usuario'),
    path("login",views.login, name='login'),
    path("register",views.register, name='register'),
    # path("transacciones",views.lista_transacciones, name='transacciones')
    
]