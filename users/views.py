from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from repex.models import Projeto, RedeSocial, IdentidadeVisual
from .models import Profile, User
from .forms import CadastroForm
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

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
def dashboard(request):
    context = {
        'projetos': Projeto.objects.all(),
        'user': request.user,
    }
    return render(request, 'dashboard.html', context)

@login_required
def paineladmin(request):
    redes_sociais = RedeSocial.objects.all()
    identidade_visual = IdentidadeVisual.objects.all()
    context = {
        'redes_sociais': redes_sociais, 
        'identidades': identidade_visual
        }
    return render(request, 'painel_admin.html', context)

class RedeSocialCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = RedeSocial
    template_name = 'rede_social_form.html'
    fields = ['nome', 'icone', 'url_base']
    success_message = 'Rede social criada com sucesso!'
    success_url = reverse_lazy('painel')

class RedeSocialUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = RedeSocial
    template_name = 'rede_social_form.html'
    fields = ['nome', 'icone', 'url_base']
    success_message = 'Rede social atualizada com sucesso!'
    success_url = reverse_lazy('painel')

class PerfilUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = 'perfil_update.html'
    fields = ['bio', 'avatar']
    success_message = 'Perfil atualizado com sucesso!'
    success_url = reverse_lazy('dashboard')

class IdentidadeVisualCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = IdentidadeVisual
    template_name = 'identidade_visual_form.html'
    fields = ['logo', 'cor_sistema', 'cor_suplente', 'cor_titulo']
    success_message = 'Identidade visual criada com sucesso!'
    success_url = reverse_lazy('painel')

class IdentidadeVisualUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = IdentidadeVisual
    template_name = 'identidade_visual_form.html'
    fields = ['logo', 'cor_sistema', 'cor_suplente', 'cor_titulo']
    success_message = 'Identidade visual atualizada com sucesso!'
    success_url = reverse_lazy('painel')