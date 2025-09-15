from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import Projeto, FotoProjeto, IdentidadeVisual
from crispy_forms.layout import Layout, Field
from crispy_forms.helper import FormHelper
from tinymce.widgets import TinyMCE

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class ProjetoForm(forms.ModelForm):
    fotos = forms.FileField(
        widget=MultiFileInput(attrs={
            "class": "form-control", 
            "multiple": True, 
            "name": "fotos",
            }), 
        required=False, 
        label="Fotos extras (opcional):"
    )
    class Meta:
        model = Projeto
        fields = [
            "titulo",
            "descricao",
            "resumo",
            "justificativa",
            "area_conhecimento",
            "objetivo",
            "resultados",
            "capa",
            "fotos",
            "doc",
            "palavras_chave",
            "status",
            "modalidade",
            "componentes",
        ]

        labels = {
            "titulo": "Título:",
            "descricao": "Descrição:",
            "resumo": "Resumo:",
            "justificativa": "Justificativa:",
            "area_conhecimento": "Área de Conhecimento:",
            "objetivo": "Objetivo:",
            "resultados": "Resultados:",
            "capa": "Capa (opcional):",
            "fotos": "Fotos extras (opcional):",
            "doc": "Documento (opcional):",
            "palavras_chave": "Palavras-chave (separadas por vírgula):",
            "status": "Status:",
            "modalidade": "Modalidade:",
            "componentes": "Componentes:",
        }

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "rows": 3, }),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "resumo": TinyMCE(attrs={"cols": 80, "rows": 10}),
            "justificativa": TinyMCE(attrs={"cols": 80, "rows": 10}),
            "area_conhecimento": forms.Select(attrs={"class": "form-select"}),
            "objetivo": TinyMCE(attrs={"cols": 80, "rows": 10}),
            "resultados": TinyMCE(attrs={"cols": 80, "rows": 10}),
            "capa": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "doc": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "palavras_chave": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "modalidade": forms.Select(attrs={"class": "form-select"}),
            "componentes": Select2MultipleWidget(attrs={"class": "form-control"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fields = list(self.fields.keys())
        fields.insert(fields.index("capa") + 1, fields.pop(fields.index("fotos")))
        self.fields = {k: self.fields[k] for k in fields}


class IdentidadeVisualForm(forms.ModelForm):
    class Meta:
        model = IdentidadeVisual
        fields = "__all__"

    cor_sistema = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "class":"form-control form-control-color"}))
    cor_suplente = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"type": "color", "value": "", "class":"form-control form-control-color"})
    )
    cor_titulo = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "class":"form-control form-control-color"}))