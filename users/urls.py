from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.verperfil, name='ver_perfil'),
    path('painel/', views.paineladmin, name='painel'),
]
