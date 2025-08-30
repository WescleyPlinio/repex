def identidade_visual(request):
    from repex.models import IdentidadeVisual
    identidade = IdentidadeVisual.objects.first()
    return {'identidade_visual': identidade}