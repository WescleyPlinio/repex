from django import template

register = template.Library()

@register.filter
def chunks(value, size=3):
    """
    Recebe um iterável (QuerySet ou lista) e retorna uma lista de listas
    com tamanho `size`. As sublistas são preenchidas com None quando
    necessário para garantir comprimento fixo.
    Uso no template: noticias|chunks:3
    """
    try:
        size = int(size)
    except (TypeError, ValueError):
        size = 3
    items = list(value)
    groups = []
    for i in range(0, len(items), size):
        group = items[i:i + size]
        if len(group) < size:
            group += [None] * (size - len(group))
        groups.append(group)
    return groups
