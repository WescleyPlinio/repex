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
    path('projeto/<int:pk>/', views.ProjetoDetailView.as_view(), name='projeto_detail'),
    path('noticia/<int:pk>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('novo/', ProjetoCreateView.as_view(), name='projeto_create'),
    path('<int:pk>/editar/', ProjetoUpdateView.as_view(), name='projeto_update'),
    path('<int:pk>/excluir/', ProjetoDeleteView.as_view(), name='projeto_delete'),
]



