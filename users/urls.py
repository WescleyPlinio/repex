from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . import views as users_views

urlpatterns = [
    path('login_suap/', views.login, name='login_suap'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('painel/', views.paineladmin, name='painel'),
    path('users', views.all_users, name="users"),
    path("users/<int:user_id>/toggle/", views.toggle_superuser, name="toggle_superuser"),
    path("users/<int:user_id>/toggle_prof/", views.toggle_professor, name="toggle_professor"),
    path('auth/callback/', views.auth_callback, name='auth_callback'),
    path("perfil/<int:pk>/editar/", views.PerfilUpdateView.as_view(), name="perfil_update"),
    
]
