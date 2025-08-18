from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from repex.models import Projeto

User = get_user_model()

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('verperfil')
    else:
        form = CadastroForm()
    return render(request, 'registration/cadastro.html', {'form': form})

@login_required
def verperfil(request):
    context = {
        'user': request.user,
        'projetos': Projeto.objects.all()
    }
    return render(request, 'verperfil.html', context)

@login_required
@permission_required('users.view_projetos', raise_exception=True)
def paineladmin(request):
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos,
        }
    return render(request, 'paineladmin.html', context)