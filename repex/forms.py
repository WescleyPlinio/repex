from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            "titulo",
            "resumo",
            "justificativa",
            "area_conhecimento",
            "objetivo",
            "resultados",
            "capa",
            "doc",
            "palavras_chave",
            "status",
            "modalidade",
            "componentes",
        ]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o título do projeto"}),
            "resumo": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "justificativa": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "area_conhecimento": forms.Select(attrs={"class": "form-select"}),
            "objetivo": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "resultados": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "capa": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "doc": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "palavras_chave": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "modalidade": forms.Select(attrs={"class": "form-select"}),
            "componentes": Select2MultipleWidget(attrs={"class": "form-control"}),
        }
