from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('painel/', views.paineladmin, name='painel'),
]
