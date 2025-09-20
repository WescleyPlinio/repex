from django.contrib import admin
from .models import Profile, User, UserSocialLink


class ProfileAdmin(admin.ModelAdmin):
    pass

class UserSocialLinkAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'url']
    list_filter = ['name']
    search_fields = ['user__username', 'user__email', 'name']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(User)
admin.site.register(UserSocialLink, UserSocialLinkAdmin)