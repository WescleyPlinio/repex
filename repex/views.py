from django.shortcuts import render
from repex.models import Projeto, Noticia

def index(request):
    projetos = Projeto.objects.all().order_by("criado_em")
    noticias = Noticia.objects.all()
    context = {
        "projetos": projetos,
        "noticias": noticias
    }
    return render(request, 'index.html', context)

def explorar(request):
    projetos = Projeto.objects.all()
    noticias = Noticia.objects.all()
    context = {
        "projetos": projetos,
        "noticias": noticias
    }
    return render(request, 'explorar.html', context)

def pesquisar(request):
    query = request.GET.get('q', '')
    
    resultados_titulo = Projeto.objects.filter(titulo__icontains=query)
    resultados_objetivo = Projeto.objects.filter(objetivo__icontains=query)
    resultados_resumo = Projeto.objects.filter(resumo__icontains=query)

    resultados = (resultados_titulo | resultados_objetivo | resultados_resumo).distinct()

    # paginator = Paginator(resultados, 3)
    # numero_da_pagina = request.GET.get('pagina')
    # resultados_paginados = paginator.get_page(numero_da_pagina)

    projetos_recentes = Projeto.objects.all().order_by("criado_em")[:6]

    context = {
        'resultados': resultados,
        'projetos_recentes': projetos_recentes,
        'query': query,
    }
    return render(request, 'explorar.html', context)
