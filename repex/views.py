from django.shortcuts import render
from repex.models import Projeto, Noticia

def index(request):
    projetos = Projeto.objects.all()
    noticias = Noticia.objects.all()
    context = {
        "projetos": projetos,
        "noticias": noticias
    }
    return render(request, 'index.html', context)
