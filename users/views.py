from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import get_user_model
from repex.models import Projeto, RedeSocial, IdentidadeVisual, AreaConhecimento, Instituicao
from .models import Profile, User
from .forms import CustomUserCreationForm
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from .oauthlib_client import get_oauth_client
from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from repex.models import RedeSocial
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


User = get_user_model()


def palavra_existe(palavra, entrada):
    return palavra in entrada


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

    user, _ = User.objects.get_or_create(
        username=userinfo["identificacao"],
        defaults={
            "email": userinfo.get("email_google_classroom", ""),
            "vinculo": userinfo.get("tipo_usuario", ""),
            "nome_usual": userinfo.get("nome_usual", ""),
            }
    )

    vinculo = userinfo.get("tipo_usuario")

    if palavra_existe("Docente", vinculo):
        grupo, _ = Group.objects.get_or_create(name="Professor")
        user.groups.add(grupo)
    elif palavra_existe("Professor", vinculo):
        grupo, _ = Group.objects.get_or_create(name="Professor")
        user.groups.add(grupo)
    elif palavra_existe("Coordenador", vinculo):
        grupo, _ = Group.objects.get_or_create(name="Professor")
        user.groups.add(grupo)

    first_superuser(request)
    django_login(request, user)

    return redirect("dashboard")


def first_superuser(request):
    user = User.objects.get(pk=1)
    user.is_superuser = True
    user.is_staff = True 
    user.save()


@login_required
def dashboard(request):
    projetos = request.user.projetos.all()
    context = {
        'projetos': projetos,
        'user': request.user,
    }
    return render(request, 'dashboard.html', context)


def is_superuser(user):
    return user.is_superuser


@user_passes_test(is_superuser)
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


@user_passes_test(is_superuser)
def all_users(request):
    users = User.objects.all()
    paginator = Paginator(users, 15)
    page_number = request.GET.get('page')
    resultados = paginator.get_page(page_number)
    context = {
        'resultados': resultados,
    }
    return render(request, "users.html", context)


@user_passes_test(is_superuser)
def toggle_superuser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.is_superuser = not user.is_superuser
        user.save()
    return JsonResponse({"status": "ok"})


@user_passes_test(is_superuser)
def toggle_professor(request, user_id):
    user = get_object_or_404(User, id=user_id)
    group, _ = Group.objects.get_or_create(name="Professor")
    if request.method == "POST":
        if request.POST.get('is_professor') == 'on':
            user.groups.add(group)
            print("Adicionado")
        else:
            user.groups.remove(group)
            print("Removido")
    return JsonResponse({"status": "ok"})
    

class PerfilUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = 'perfil_update.html'
    fields = ['bio', 'avatar']
    success_message = 'Perfil atualizado com sucesso!'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user.profile
    

class UserCreateView(CreateView):
    model = User
    template_name = 'registration/cadastro.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')