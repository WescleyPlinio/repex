from django.db import models


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    resumo = models.TextField(max_length=2000)
    objetivo = models.TextField(max_length=2000)
    capa = models.ImageField('media/')
    pdf = models.FileField(blank=True, null=True)
    palavras_chave = models.CharField(max_length=200, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    
class FotoProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField()

    def __str__(self):
        return f"Foto do projeto {self.projeto.titulo}"
    


