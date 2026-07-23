from django.shortcuts import render, get_object_or_404
from .models import Profissional, Servico, HorarioDisponivel
import urllib.parse

def home(request):
    # Busca os profissionais e carrega a nova página inicial da Órbita
    profissionais = Profissional.objects.all() 
    # AJUSTADO: mudamos de professionals para profissionais no final da linha abaixo
    return render(request, 'agenda/index.html', {'profissionais': profissionais})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        usuario_digitado = request.POST.get('username')
        senha_digitada = request.POST.get('password')
        
        # O Django tenta encontrar e validar o usuário no banco de dados
        user = authenticate(request, username=usuario_digitado, password=senha_digitada)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo de volta, {user.username}!")
            return redirect('home') # Redireciona de volta para a página inicial logado
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            
    return render(request, 'agenda/login.html')


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
        'profissional': profissional, 
        'servicos': servicos, 
        'horarios': horarios, 
        'whatsapp_link': whatsapp_link
    })
from django.contrib.auth.models import User
from django.http import HttpResponse

def criar_admin_temporario(request):
    if not User.objects.filter(username="admin_orbita").exists():
        User.objects.create_superuser("admin_orbita", "admin@email.com", "SenhaSuperSegura123")
        return HttpResponse("Administrador criado com sucesso! Usuário: admin_orbita | Senha: SenhaSuperSegura123")
    return HttpResponse("O administrador já existe.")
