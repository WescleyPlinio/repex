from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image, ImageOps
from django.conf import settings
from django.apps import apps

class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, null=True)

    vinculo = models.CharField(max_length=50, blank=True, null=True)
    nome_usual = models.CharField(max_length=150, blank=True, null=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def get_primeiro_nome(self):
        if self.nome_usual:
            return self.nome_usual.split(" ")[0]
        return self.username
    
    def get_ultimo_nome(self):
        if self.nome_usual:
            return self.nome_usual.split(" ")[-1]
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return self.email


def is_professor(self):
    return self.groups.filter(name="Professor").exists()

User.add_to_class("is_professor", is_professor)

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True, max_length=500)
    avatar = models.ImageField(upload_to='media', blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)

            output_size = (300, 300)
            img = ImageOps.fit(img, output_size, Image.LANCZOS)

            img.save(self.avatar.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

