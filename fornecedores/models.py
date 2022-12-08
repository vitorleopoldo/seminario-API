from django.db import models

class fornecedores(models.Model):

    id_fornecedores = models.AutoField(primary_key=True)
    pecas = models.CharField(max_length=100)
    pneus = models.CharField(max_length=100)
    oleo = models.CharField(max_length=100)
    capacetes = models.CharField(max_length=100)
    capa_chuva = models.CharField(max_length=100)

    def __str__(self):
        return self.pecas