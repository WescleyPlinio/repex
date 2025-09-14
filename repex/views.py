from django.shortcuts import render, redirect
from .models import Projeto, Noticia, IdentidadeVisual, FotoProjeto, AreaConhecimento, Instituicao
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import ProjetoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from users.models import User
from django.db.models import Q


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
    status = request.GET.get('status')
    modalidade = request.GET.get('modalidade')

    resultado_projeto_titulo = Projeto.objects.filter(titulo__icontains=query)
    resultado_projeto_objetivo = Projeto.objects.filter(objetivo__icontains=query)
    resultado_projeto_resumo = Projeto.objects.filter(resumo__icontains=query)
    resultados_projetos = (resultado_projeto_titulo | resultado_projeto_objetivo | resultado_projeto_resumo).distinct()

    resultado_noticia_titulo = Noticia.objects.filter(titulo__icontains=query)
    resultado_noticia_descricao = Noticia.objects.filter(descricao__icontains=query)
    resultado_noticia_conteudo = Noticia.objects.filter(conteudo__icontains=query)
    resultados_noticias = (resultado_noticia_titulo | resultado_noticia_descricao | resultado_noticia_conteudo).distinct()
    
    if status:
        resultados_projetos = resultados_projetos.filter(status=status).distinct()
    if modalidade:
        resultados_projetos = resultados_projetos.filter(modalidade=modalidade).distinct()

    paginator_projetos = Paginator(resultados_projetos, 6)
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
        'status_choices': Projeto.STATUS_CHOICES,
        'modalidade_choices': Projeto.MODALIDADE_CHOICES,
    }
    return render(request, 'explorar.html', context)


def ajax_projetos(request):
    query = request.GET.get('q', '')
    status = request.GET.get('status', '')
    modalidade = request.GET.get('modalidade', '')

    resultado_projeto_titulo = Projeto.objects.filter(titulo__icontains=query)
    resultado_projeto_objetivo = Projeto.objects.filter(objetivo__icontains=query)
    resultado_projeto_resumo = Projeto.objects.filter(resumo__icontains=query)
    resultados_projetos = (
        resultado_projeto_titulo | resultado_projeto_objetivo | resultado_projeto_resumo
    ).distinct()

    if status:
        resultados_projetos = resultados_projetos.filter(status=status)
    if modalidade:
        resultados_projetos = resultados_projetos.filter(modalidade=modalidade)

    paginator = Paginator(resultados_projetos, 6)
    page_number = request.GET.get('page_projetos')
    page_obj = paginator.get_page(page_number)

    html = render_to_string(
        "partials/_ajax_projetos.html",
        {
            "resultados_projetos": page_obj,
            "query": query,
        },
        request=request,
    )

    return JsonResponse({"html": html})


def buscar_projetos(request):
    query = request.GET.get('q', '')
    resultados = Projeto.objects.filter(nome__icontains=query) if query else []
    data = [{"id": p.id, "nome": p.nome} for p in resultados]
    return JsonResponse(data, safe=False)


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


class ProjetoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'projeto_form.html'
    success_message = 'Projeto criado com sucesso!'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        self.object = form.save()
        self.object.componentes.add(self.request.user)

        for file in self.request.FILES.getlist("fotos"):
            FotoProjeto.objects.create(projeto=self.object, foto=file)
        return super().form_valid(form)


class NoticiaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Noticia
    fields = ['titulo', 'descricao', 'conteudo', 'imagem', 'area_conhecimento']
    template_name = 'noticia_form.html'
    success_message = 'Notícia criada com sucesso!'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    

class AreaConhecimentoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AreaConhecimento
    fields = ['area']
    template_name = 'area_conhecimento_form.html'
    success_message = 'Área de conhecimento cadastrada com sucesso!'
    success_url = reverse_lazy('painel')


class InstituicaoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Instituicao
    fields = ['logo', 'nome', 'cep', 'endereco', 'site']
    template_name = 'instituicao_form.html'
    success_message = 'Instituição cadastrada com sucesso!'
    success_url = reverse_lazy('painel')


class ProjetoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'projeto_form.html'
    success_message = 'Projeto atualizado com sucesso!'
    success_url = reverse_lazy('dashboard')


class NoticiaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Noticia
    fields = ['titulo', 'descricao', 'conteudo', 'imagem', 'area_conhecimento']
    template_name = 'noticia_form.html'
    success_message = 'Notícia atualizada com sucesso!'
    success_url = reverse_lazy('dashboard')


class AreaConhecimentoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AreaConhecimento
    fields = ['area']
    template_name = 'area_conhecimento_form.html'
    success_message = 'Áre de conhecimento atualizada com sucesso!'
    success_url = reverse_lazy('painel')

class InstituicaoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Instituicao
    fields = ['logo', 'nome', 'cep', 'endereco', 'site']
    template_name = 'instituicao_form.html'
    success_message = 'Instituição atualizada com sucesso!'
    success_url = reverse_lazy('painel')


class ProjetoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Projeto
    template_name = 'projeto_confirm_delete.html'
    success_url = reverse_lazy('dashboard')


class NoticiaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Noticia
    template_name = 'noticia_confirm_delete.html'
    success_url = reverse_lazy('dashboard')


class AreaConhecimentoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = AreaConhecimento
    template_name = 'area_conhecimento_confirm_delete.html'
    success_url = reverse_lazy('painel')


class InstituicaoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Instituicao
    template_name = 'instituicao_confirm_delete.html'
    success_url = reverse_lazy('painel')
    

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile_detail.html'
    context_object_name = 'user'