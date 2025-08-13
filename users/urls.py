from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Autenticação
    path('login/',  auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Cadastro
    path('cadastro/', views.cadastro, name='cadastro'),

    # Perfil
    path('perfil/', views.verperfil, name='verperfil'),

    # Painel "admin" simples
    path('painel/', views.paineladmin, name='painel'),
]
