from django import forms
from .models import UserSocialLink

class UserSocialLinkForm(forms.ModelForm):
    class Meta:
        model = UserSocialLink
        fields = ["name", "url"]
        widgets = {
            'name': forms.Select(choices=[
                ('', 'Selecione a rede social'),
                ('Instagram', 'Instagram'),
                ('Facebook', 'Facebook'),
                ('Twitter', 'Twitter'),
                ('LinkedIn', 'LinkedIn'),
                ('GitHub', 'GitHub'),
                ('YouTube', 'YouTube'),
                ('Outra', 'Outra'),
            ]),
            'url': forms.URLInput(attrs={'placeholder': 'https://...'})
        }