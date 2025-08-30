from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path("editar_perfil/<int:pk>", views.PerfilUpdate.as_view(), name="editar_perfil"),
    path('painel/', views.paineladmin, name='painel'),
    path('nova_rede_social/', views.RedeSocialCreate.as_view(), name='nova_rede_social'),
    path('editar_rede_social/<int:pk>/', views.RedeSocialUpdate.as_view(), name='editar_rede_social'),
    path('identidade_visual/nova/', views.IdentidadeVisualCreateView.as_view(), name='identidade_visual_create'),
    path('identidade_visual/<int:pk>/editar/', views.IdentidadeVisualUpdateView.as_view(), name='identidade_visual_update'),
]
