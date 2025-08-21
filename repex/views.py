from django.shortcuts import render
from repex.models import Projeto, Noticia
from django.views.generic import DetailView

def index(request):
    projetos = Projeto.objects.all().order_by("criado_em")[:9]
    noticias = Noticia.objects.all()
    context = {
        "projetos": projetos,
        "noticias": noticias
    }
    return render(request, 'index.html', context)

def explorar(request):
    query = request.GET.get('q', '')
    
    resultado_projeto_titulo = Projeto.objects.filter(titulo__icontains=query)
    resultado_projeto_objetivo = Projeto.objects.filter(objetivo__icontains=query)
    resultado_projeto_resumo = Projeto.objects.filter(resumo__icontains=query)

    resultado_noticia_titulo = Noticia.objects.filter(titulo__icontains=query)
    resultado_noticia_descricao = Noticia.objects.filter(descricao__icontains=query)
    resultado_noticia_conteudo = Noticia.objects.filter(conteudo__icontains=query)

    resultados_projetos = (resultado_projeto_titulo | resultado_projeto_objetivo | resultado_projeto_resumo).distinct()
    resultados_noticias = (resultado_noticia_titulo | resultado_noticia_descricao | resultado_noticia_conteudo).distinct()

    # paginator = Paginator(resultados, 3)
    # numero_da_pagina = request.GET.get('pagina')
    # resultados_paginados = paginator.get_page(numero_da_pagina)

    projetos_random = Projeto.objects.all().order_by("?")[:9]
    noticias_random = Noticia.objects.all().order_by("?")[:9]

    context = {
        'resultados_projetos': resultados_projetos,
        'resultados_noticias': resultados_noticias,
        'projetos_random': projetos_random,
        'noticias_random': noticias_random,
        'query': query,
    }
    return render(request, 'explorar.html', context)

class ProjetoDetailView(DetailView):
    model = Projeto
    template_name = 'projeto_detail.html'
    context_object_name = 'projeto'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticia_detail.html'
    context_object_name = 'noticia'
