from django.db import models

class funcionarios(models.Model):

    id_funcionarios = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    dataNascimento = models.CharField(max_length=100)
    salario = models.CharField(max_length=100)
    horas = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome