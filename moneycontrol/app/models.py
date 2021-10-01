from django.db import models

class Despesas(models.Model):
    nome = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255,null=True,blank=True)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True,blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nome

# Create your models here.
