from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from repex.models import Projeto, RedeSocial, IdentidadeVisual, AreaConhecimento, Instituicao
from .models import Profile, User
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .oauthlib_client import get_oauth_client
from django.conf import settings

User = get_user_model()

def login(request):
    oauth = get_oauth_client("suap")
    provider = settings.OAUTH_PROVIDERS["suap"]
    uri, state = oauth.create_authorization_url(provider["authorize_url"])
    request.session["oauth_state"] = state
    return redirect(uri)

def logout(request):
    django_logout(request)
    return redirect('index')

def auth_callback(request):
    client = get_oauth_client("suap")
    token = client.fetch_token(
        settings.OAUTH_PROVIDERS["suap"]["access_token_url"],
        authorization_response=request.build_absolute_uri()
    )

    resp = client.get(settings.OAUTH_PROVIDERS["suap"]["userinfo_url"])
    userinfo = resp.json()
    print(userinfo)

    user, _ = User.objects.get_or_create(
        username=userinfo["identificacao"],
        defaults={
            "email": userinfo.get("email_google_classroom", ""),
            "vinculo": userinfo.get("tipo_usuario", ""),
            "nome_usual": userinfo.get("nome_usual", ""),
            }
    )

    django_login(request, user)

    return redirect("dashboard")

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
    area_conhecimento = AreaConhecimento.objects.all()
    instituicao = Instituicao.objects.all()
    context = {
        'redes_sociais': redes_sociais, 
        'identidades': identidade_visual,
        'areas': area_conhecimento,
        'instituicoes': instituicao,
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