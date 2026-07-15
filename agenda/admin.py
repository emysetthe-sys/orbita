from django.contrib import admin
from .models import Profissional, Servico, HorarioDisponivel

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nicho', 'whatsapp')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissional', 'preco_base')

@admin.register(HorarioDisponivel)
class HorarioDisponivelAdmin(admin.ModelAdmin):
    list_display = ('profissional', 'data', 'hora', 'disponivel')
    list_editable = ('disponivel',)  # Permite dar baixa manual clicando direto na lista!
