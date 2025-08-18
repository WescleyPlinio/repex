from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class User(AbstractUser):
    nome_completo = models.CharField(max_length=200, null=True, blank=True)
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)