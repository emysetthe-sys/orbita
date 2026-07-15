from django.shortcuts import render, get_object_or_404
from .models import Profissional, Servico, HorarioDisponivel
import urllib.parse

def lista_profissionais(request):
    profissionais = Profissional.objects.all()
    return render(request, 'agenda/index.html', {'profissionais': profissionais})

def perfil_profissional(request, profissional_id):
    profissional = get_object_or_404(Profissional, pk=profissional_id)
    servicos = profissional.servicos.all()
    horarios = profissional.horarios.filter(disponivel=True)
    whatsapp_link = None
    
    if request.method == 'POST':
        servico_id = request.POST.get('servico')
        horario_id = request.POST.get('horario')
        
        servico_escolhido = Servico.objects.get(pk=servico_id)
        horario_escolhido = HorarioDisponivel.objects.get(pk=horario_id)
        
        # Dá baixa automática no horário tirando-o do site
        horario_escolhido.disponivel = False
        horario_escolhido.save()
        
        # Cria a mensagem personalizada para o WhatsApp
        texto = f"Olá {profissional.nome}! Quero agendar o serviço '{servico_escolhido.nome}' (Valor base: R${servico_escolhido.preco_base}) para o dia {horario_escolhido.data} às {horario_escolhido.hora}."
        texto_codificado = urllib.parse.quote(texto)
        whatsapp_link = f"https://wa.me{profissional.whatsapp}?text={texto_codificado}"

    return render(request, 'agenda/perfil.html', {
        'profissional': profissional, 'servicos': servicos, 'horarios': horarios, 'whatsapp_link': whatsapp_link
    })
