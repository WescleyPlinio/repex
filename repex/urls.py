from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explorar/', views.explorar, name='explorar'),
    path("pesquisar/", views.pesquisar, name = "pesquisar"),
]