from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Endereco(models.Model):
    endereco = models.CharField(
        'endereço',
        max_length=100,
        null=True,
        blank=True
    )
    complemento = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True
    )
    bairro = models.CharField(
        'bairro',
        max_length=100,
        null=True,
        blank=True
    )
    cidade = models.CharField('cidade', max_length=100, null=True, blank=True)
    uf = models.CharField(
        'UF',
        max_length=2,
        choices=STATE_CHOICES,
        null=True,
        blank=True
    )
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)

    class Meta:
        abstract = True
