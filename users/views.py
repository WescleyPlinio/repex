from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from repex.models import Projeto, RedeSocial, IdentidadeVisual
from .models import Profile, User
from .forms import CadastroForm
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy

User = get_user_model()

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = CadastroForm()
    return render(request, "registration/cadastro.html", {"form": form})

@login_required
def ver_perfil(request):
    context = {
        'projetos': Projeto.objects.all(),
        'user': request.user,
    }
    return render(request, 'ver_perfil.html', context)

@login_required
def paineladmin(request):
    redes_sociais = RedeSocial.objects.all()
    identidade_visual = IdentidadeVisual.objects.all()
    context = {
        'redes_sociais': redes_sociais, 
        'identidades': identidade_visual
        }
    return render(request, 'paineladmin.html', context)

class RedeSocialCreate(CreateView):
    model = RedeSocial
    template_name = 'form_rede_social.html'
    fields = ['nome', 'icone', 'url_base']
    success_url = reverse_lazy('painel')

class RedeSocialUpdate(UpdateView):
    model = RedeSocial
    template_name = 'form_rede_social.html'
    fields = ['nome', 'icone', 'url_base']
    success_url = reverse_lazy('painel')

class PerfilUpdate(UpdateView):
    model = Profile
    template_name = 'editar_perfil.html'
    fields = ['bio', 'avatar']
    success_url = reverse_lazy('ver_perfil')

class IdentidadeVisualCreateView(CreateView):
    model = IdentidadeVisual
    fields = ['logo', 'cor_sistema', 'cor_suplente', 'cor_titulo']
    template_name = 'identidade_visual_form.html'
    success_message = 'Identidade visual criada com sucesso!'
    success_url = reverse_lazy('painel')

class IdentidadeVisualUpdateView(UpdateView):
    model = IdentidadeVisual
    fields = ['logo', 'cor_sistema', 'cor_suplente', 'cor_titulo']
    template_name = 'identidade_visual_form.html'
    success_message = 'Identidade visual atualizada com sucesso!'
    success_url = reverse_lazy('painel')