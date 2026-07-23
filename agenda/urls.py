from django.urls import path, include
from . import views

urlpatterns = [
    # 1. Página inicial com o novo design galáctico
    path('', views.home, name='home'),
    
    # 2. Tela de Login com as opções do Google e Facebook
    path('login/', views.login_view, name='login'),
    
    # 3. Página de perfil/agenda de cada profissional
    path('profissional/<int:profissional_id>/', views.perfil_profissional, name='perfil_profissional'),
    
    # 4. Rota corrigida e limpa para login social
    path('social-auth/', include('social_django.urls', namespace='social')),
]
path('criar-admin-secreto/', views.criar_admin_temporario),
