def identidade_visual(request):
    from repex.models import IdentidadeVisual
    identidade = IdentidadeVisual.objects.first()
    return {'identidade_visual': identidade}


def instituicao(request):
    from repex.models import Instituicao
    instituicao = Instituicao.objects.first()
    return {'instituicao': instituicao}