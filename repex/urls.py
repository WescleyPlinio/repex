from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explorar/', views.explorar, name='explorar'),
    path('projeto/<int:pk>/', views.ProjetoDetailView.as_view(), name='projeto_detail'),
    path('noticia/<int:pk>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
]