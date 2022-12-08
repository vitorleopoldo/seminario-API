from django.db import models

class produtos(models.Model):

    id_produtos = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    kit_relacao = models.CharField(max_length=100)
    pneu = models.CharField(max_length=100)
    retrovisor = models.CharField(max_length=100)
    painel = models.CharField(max_length=100)
    oleo = models.CharField(max_length=100)


    def __str__(self):
        return self.nome_produto