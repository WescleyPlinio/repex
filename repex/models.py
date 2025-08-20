from django.db import models
from users.models import Profile, User

class AreaConhecimento(models.Model):
    area = models.CharField(max_length=150)

    def __str__(self):
        return self.area

class Projeto(models.Model):
    STATUS_CHOICES = [
        ("Em andamento", "Em andamento"),
        ("Concluído", "Concluído"),
    ]
    MODALIDADE_CHOICES = [
        ("Ensino", "Ensino"),
        ("Pesquisa", "Pesquisa"),
        ("Extensão", "Extensão"),
    ]

    titulo = models.CharField(max_length=100)
    resumo = models.TextField(max_length=3000)
    justificativa = models.TextField(max_length=2000)
    area_conhecimento = models.ForeignKey(AreaConhecimento, on_delete=models.CASCADE, related_name='area_conhecimento', null=True, blank=True)
    objetivo = models.TextField(max_length=2000)
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    resultados = models.TextField(max_length=3000)
    capa = models.ImageField(upload_to='media/', null=True, blank=True)
    doc = models.FileField(blank=True, null=True)
    palavras_chave = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    modalidade = models.CharField(max_length=20, choices=MODALIDADE_CHOICES)
    componentes = models.ManyToManyField(User, related_name='projetos', blank=True)
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    
class FotoProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField()

    def __str__(self):
        return f"Foto do projeto {self.projeto.titulo}"

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    conteudo = models.TextField(max_length=3000)
    data_publicacao = models.DateTimeField(auto_now_add=True, null=True)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)
    area_conhecimento = models.ForeignKey(AreaConhecimento, on_delete=models.CASCADE, related_name='area_conhecimento_noticia', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noticias', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# class SocialNetwork(models.Model):
#     """
#     Cadastrado pelo admin: lista de redes possíveis.
#     """
#     nome = models.CharField(max_length=100, unique=True)
#     icone = models.CharField(max_length=50, blank=True, null=True)  # Ex: fa-brands fa-instagram
#     url_base = models.URLField(blank=True, null=True)  # Ex: "https://instagram.com/"

#     def __str__(self):
#         return self.nome


# class UserSocialLink(models.Model):
#     """
#     O usuário escolhe a rede e cadastra o próprio link/perfil.
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="social_links")
#     rede = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE)
#     url = models.URLField("URL do perfil")

#     class Meta:
#         unique_together = ("user", "rede")  # Garante que cada user só tenha 1 link por rede

#     def __str__(self):
#         return f"{self.user.username} - {self.rede.nome}"
