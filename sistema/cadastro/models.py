from django.db import models

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True) 
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return '%s' % self.nome


class Projeto(models.Model):
    id = models.IntegerField(primary_key=True) 
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=255)
    status = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.nome


class Cargo(models.Model):
    id = models.IntegerField(primary_key=True) 
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    id = models.IntegerField(primary_key=True) 
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    codigo = models.IntegerField(unique=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.nome
