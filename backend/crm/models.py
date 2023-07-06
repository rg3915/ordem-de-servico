from django.db import models
from django.urls import reverse_lazy

from backend.core.models import Endereco


class Cliente(Endereco):
    razao_social = models.CharField('Razão Social', max_length=120, unique=True)
    cnpj = models.CharField('CNPJ', max_length=14, null=True, blank=True)

    class Meta:
        ordering = ('razao_social',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return f'{self.razao_social}'

    def get_absolute_url(self):
        return reverse_lazy('crm:cliente_detail', kwargs={'pk': self.pk})
