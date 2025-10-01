from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User 

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