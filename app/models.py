from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100)

    def __str__(self):
        return self.nome
