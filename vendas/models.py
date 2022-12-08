from django.db import models

class vendas(models.Model):

    id_vendas = models.AutoField(primary_key=True)
    clientes = models.CharField(max_length=100)
    produtos = models.CharField(max_length=100)
    compra = models.CharField(max_length=100)
    valor = models.CharField(max_length=11)
    data = models.CharField(max_length=100)

    def __str__(self):
        return self.clientes