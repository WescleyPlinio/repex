from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explorar/', views.explorar, name='explorar'),
    path("ajax_projetos/", views.ajax_projetos, name="ajax_projetos"),
    path("ajax_noticias/", views.ajax_noticias, name="ajax_noticias"),
    path('projeto/<int:pk>/', views.ProjetoDetailView.as_view(), name='projeto_detail'),
    path('noticia/<int:pk>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
]