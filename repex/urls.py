from django.contrib import admin
from django.urls import path, include
from . import views 
from .views import (
    ProjetoCreateView, ProjetoUpdateView, ProjetoDeleteView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('explorar/', views.explorar, name='explorar'),
    path("ajax_noticias/", views.ajax_noticias, name="ajax_noticias"),
    path("ajax_projetos/", views.ajax_projetos, name="ajax_projetos"),
    path('noticia/<int:pk>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('projeto/<int:pk>/', views.ProjetoDetailView.as_view(), name='projeto_detail'),
    path('projeto/novo/', ProjetoCreateView.as_view(), name='projeto_create'),
    path('projeto/<int:pk>/editar/', ProjetoUpdateView.as_view(), name='projeto_update'),
    path('projeto/<int:pk>/excluir/', ProjetoDeleteView.as_view(), name='projeto_delete'),

]



