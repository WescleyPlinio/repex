from django.shortcuts import render
from repex.models import Projeto, Noticia
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import JsonResponse

def index(request):
    projetos = Projeto.objects.all().order_by("criado_em")[:9]
    noticias = Noticia.objects.all().order_by("criado_em")[:9]
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
    resultados_projetos = (resultado_projeto_titulo | resultado_projeto_objetivo | resultado_projeto_resumo).distinct()

    resultado_noticia_titulo = Noticia.objects.filter(titulo__icontains=query)
    resultado_noticia_descricao = Noticia.objects.filter(descricao__icontains=query)
    resultado_noticia_conteudo = Noticia.objects.filter(conteudo__icontains=query)
    resultados_noticias = (resultado_noticia_titulo | resultado_noticia_descricao | resultado_noticia_conteudo).distinct()

    paginator_projetos = Paginator(resultados_projetos, 3)
    page_number_projetos = request.GET.get('page_projetos')
    resultados_projetos = paginator_projetos.get_page(page_number_projetos)

    paginator_noticias = Paginator(resultados_noticias, 3)
    page_number_noticias = request.GET.get('page_noticias')
    resultados_noticias = paginator_noticias.get_page(page_number_noticias)

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

def ajax_projetos(request):
    query = request.GET.get('q', '')

    resultado_projeto_titulo = Projeto.objects.filter(titulo__icontains=query)
    resultado_projeto_objetivo = Projeto.objects.filter(objetivo__icontains=query)
    resultado_projeto_resumo = Projeto.objects.filter(resumo__icontains=query)
    resultados_projetos = (resultado_projeto_titulo | resultado_projeto_objetivo | resultado_projeto_resumo).distinct()

    paginator = Paginator(resultados_projetos, 3)
    page_number = request.GET.get('page_projetos')
    page_obj = paginator.get_page(page_number)

    html = render_to_string(
        "partials/_ajax_projetos.html",
        {"resultados_projetos": page_obj, "query": query},
        request=request
    )

    return JsonResponse({"html": html})

def ajax_noticias(request):
    query = request.GET.get('q', '')

    resultado_noticia_titulo = Noticia.objects.filter(titulo__icontains=query)
    resultado_noticia_descricao = Noticia.objects.filter(descricao__icontains=query)
    resultado_noticia_conteudo = Noticia.objects.filter(conteudo__icontains=query)
    resultados_noticias = (resultado_noticia_titulo | resultado_noticia_descricao | resultado_noticia_conteudo).distinct()

    paginator = Paginator(resultados_noticias, 3)
    page_number = request.GET.get('page_noticias')
    page_obj = paginator.get_page(page_number)

    html = render_to_string(
        "partials/_ajax_noticias.html",
        {"resultados_noticias": page_obj, "query": query},
        request=request
    )

    return JsonResponse({"html": html})

class ProjetoDetailView(DetailView):
    model = Projeto
    template_name = 'projeto_detail.html'
    context_object_name = 'projeto'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticia_detail.html'
    context_object_name = 'noticia'
