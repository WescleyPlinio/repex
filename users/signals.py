from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission

@receiver(post_migrate)
def grupos_padrao(sender, **kwargs):
    
    professor, _ = Group.objects.get_or_create(name="Professor")
    perms_professor = [
        "view_user", "add_projeto", "view_projeto", "change_projeto",
        "delete_projeto", "add_noticia", "view_noticia", "change_noticia",
        "delete_noticia", 
    ]
    for codename in perms_professor:
        try:
            perm = Permission.objects.get(codename=codename)
            professor.permissions.add(perm)
        except Permission.DoesNotExist:
            pass
