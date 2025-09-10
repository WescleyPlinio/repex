from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/authorized/', views.auth, name='login/authorized'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('painel/', views.paineladmin, name='painel'),
    path('rede_social/nova/', views.RedeSocialCreate.as_view(), name='rede_social_create'),
    path('identidade_visual/nova/', views.IdentidadeVisualCreateView.as_view(), name='identidade_visual_create'),
    path("perfil/<int:pk>/editar/", views.PerfilUpdateView.as_view(), name="perfil_update"),
    path('rede_social/<int:pk>/editar', views.RedeSocialUpdate.as_view(), name='rede_social_update'),
    path('identidade_visual/<int:pk>/editar/', views.IdentidadeVisualUpdateView.as_view(), name='identidade_visual_update'),
]
