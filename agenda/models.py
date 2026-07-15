from django.db import models

class Profissional(models.Model):
    NICHOS = [
        ('FOTO', 'Fotógrafo'),
        ('TRAN', 'Trancista'),
        ('BARB', 'Barbeiro'),
        ('EVEN', 'Produtor de Eventos'),
    ]
    nome = models.CharField(max_length=100)
    nicho = models.CharField(max_length=4, choices=NICHOS)
    foto = models.ImageField(upload_to='profissionais/', blank=True, null=True, help_text="Suba a foto do profissional")
    whatsapp = models.CharField(max_length=15, help_text="Ex: 5584999999999")
    bio = models.TextField()

    def __str__(self):
        return self.nome

class Servico(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='servicos')
    nome = models.CharField(max_length=100)
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.profissional.nome}"

class HorarioDisponivel(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='horarios')
    data = models.DateField()
    hora = models.TimeField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.data} às {self.hora} - {self.profissional.nome}"
