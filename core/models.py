from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empresas(models.Model):

    class Meta:

        db_table = 'empresas'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome_fantasia']

    nome_fantasia = models.CharField(max_length=255, null=False, blank=False)
    localizacao = models.CharField(max_length=255, null=False, blank=False)
    razao_social = models.CharField(max_length=255, null=False, blank=False)
    cnpj = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome

class Funcionarios(User):

    class Meta:

        db_table = 'funcionarios'
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    cargo = models.CharField(max_length=255, null=False, blank=False)
    idade = models.IntegerField(null=False, blank=False)
    empresa = models.ManyToManyField(Empresas, related_name='funcionarios', blank=True)

    def __str__(self):
        return self.nome
