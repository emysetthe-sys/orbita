from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_profissionais, name='lista_profissionais'),
    path('profissional/<int:profissional_id>/', views.perfil_profissional, name='perfil_profissional'),
]

