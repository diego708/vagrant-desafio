from django.db import models

from cadastro.models import Projeto, Cliente, Funcionario

class Atividade(models.Model):
    id = models.IntegerField(primary_key=True) 
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=255)
    status = models.BooleanField()
    responsavel = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    