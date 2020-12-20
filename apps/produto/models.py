from django.db import models


# Create your models here.
from django.urls import reverse


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_produto')

