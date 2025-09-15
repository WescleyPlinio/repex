from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('explorar/', views.explorar, name='explorar'),
    path("ajax_noticias/", views.ajax_noticias, name="ajax_noticias"),
    path("ajax_projetos/", views.ajax_projetos, name="ajax_projetos"),
    path('noticia/<int:pk>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('projeto/<int:pk>/', views.ProjetoDetailView.as_view(), name='projeto_detail'),
    path('projeto/novo/', views.ProjetoCreateView.as_view(), name='projeto_create'),
    path('noticia/novo/', views.NoticiaCreateView.as_view(), name='noticia_create'),
    path('area_conhecimento/nova/', views.AreaConhecimentoCreateView.as_view(), name='area_conhecimento_create'),
    path('instituicao/nova/', views.InstituicaoCreateView.as_view(), name='instituicao_create'),
    path('identidade_visual/nova/', views.IdentidadeVisualCreateView.as_view(), name='identidade_visual_create'),
    path('noticia/<int:pk>/editar/', views.NoticiaUpdateView.as_view(), name='noticia_update'),
    path('projeto/<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='projeto_update'),
    path('area_conhecimento/<int:pk>/editar/', views.AreaConhecimentoUpdateView.as_view(), name='area_conhecimento_update'),
    path('instituicao/<int:pk>/editar/', views.InstituicaoUpdateView.as_view(), name='instituicao_update'),
    path('identidade_visual/<int:pk>/editar/', views.IdentidadeVisualUpdateView.as_view(), name='identidade_visual_update'),
    path('projeto/<int:pk>/excluir/', views.ProjetoDeleteView.as_view(), name='projeto_delete'),
    path('noticia/<int:pk>/excluir/', views.NoticiaDeleteView.as_view(), name='noticia_delete'),
    path('area_conhecimento/<int:pk>/excluir/', views.AreaConhecimentoDeleteView.as_view(), name='area_conhecimento_delete'),
    path('instituicao/<int:pk>/excluir/', views.InstituicaoDeleteView.as_view(), name='instituicao_delete'),

]



