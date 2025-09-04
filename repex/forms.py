from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import Projeto, FotoProjeto
from crispy_forms.layout import Layout, Field

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
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fields = list(self.fields.keys())
        fields.insert(fields.index("capa") + 1, fields.pop(fields.index("fotos")))
        self.fields = {k: self.fields[k] for k in fields}