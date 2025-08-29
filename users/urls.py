from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path("editar_perfil/<int:pk>", views.PerfilUpdate.as_view(), name="editar_perfil"),
    path('painel/', views.paineladmin, name='painel'),
]
