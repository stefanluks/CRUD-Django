from django import forms
from django.db import models
from django.contrib.auth.models import User

#Lista de Tarefa relacionada ao Usuario do django

class Lista(models.Model):
    nome = models.CharField("Nome da Lista",max_length=50)
    descricao = models.TextField("Descrição", max_length=500, null=True, blank=True)
    corBg = models.CharField("Cor Do Background em Hexadecimal", max_length=500, null=True, blank=True)
    corTt = models.CharField("Cor do Titulo em Hexadecimal", max_length=500, null=True, blank=True)
    corTx = models.CharField("Cor dos textos em Hexadecimal", max_length=500, null=True, blank=True)
    dono = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def GetTarefas(self):
        return Tarefa.objects.filter(pertence=self)

# Tarefas em que o usuario pode criar dentro de cada Lista

class Tarefa(models.Model):
    texto = models.CharField("Tarefa",max_length=300)
    concluido = models.BooleanField("Está Concluido",default=False)
    pertence = models.ForeignKey(Lista,on_delete=models.CASCADE)

    def __str__(self):
        return self.pertence.nome + " - Tarefa - id:" + str(self.pk)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","password"]