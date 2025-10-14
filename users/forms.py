from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Submit

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'nome_usual')
        widgets = {
            'nome_usual': forms.TextInput(attrs={'placeholder': 'Exemplo: Wescley Galdino'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_usual'].required = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='col-12 col-lg-6 mb-3'),
                Column('nome_usual', css_class='col-12 col-lg-6 mb-3'),
            ),
            Row(
                Column('password1', css_class='col-12 col-lg-6 mb-3'),
                Column('password2', css_class='col-12 col-lg-6 mb-3'),
            ),
            Row(
                Column(
                    Submit('submit', 'Cadastrar', css_class='btn-primary w-100'),
                    css_class='col-12'
                ),
            )
        )