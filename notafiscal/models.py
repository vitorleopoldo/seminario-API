from django.db import models

class notafiscal(models.Model):

    id_notafiscal = models.AutoField(primary_key=True)
    nota = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    preco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    data = models.CharField(max_length=100)

    def __str__(self):
        return self.nota