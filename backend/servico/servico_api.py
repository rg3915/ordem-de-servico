from datetime import date
from decimal import Decimal
from http import HTTPStatus
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja.orm import create_schema

from backend.crm.models import Cliente
from backend.servico.models import OrdemServico, OrdemServicoItem, Servico

router = Router()


ServicoSchema = create_schema(Servico, fields=(
    'id',
    'titulo',
))


class OrdemServicoItemSchemaIn(Schema):
    ordem_servico_id: int = None
    servico_id: int
    valor: Decimal = None
    proxima_visita: date = None


class OrdemServicoSchemaIn(Schema):
    situacao: str
    cliente_id: int = None
    ordem_servico_itens: List[OrdemServicoItemSchemaIn]


@router.get('servico/', response=List[ServicoSchema])
def list_servico(request, search=None):
    if search:
        return Servico.objects.filter(titulo__istartswith=search)
    return Servico.objects.all()


@router.post('ordem-servico/')
def create_ordem_servico(request, payload: OrdemServicoSchemaIn):
    data = payload.dict()

    situacao = data.get('situacao')
    cliente_id = data.get('cliente_id')

    # Todos são equivalentes
    # cliente = Cliente.objects.get(pk=cliente_id)
    # cliente = Cliente.objects.filter(pk=cliente_id).first()
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    # Cria a OrdemServico
    ordem_servico = OrdemServico.objects.create(situacao=situacao, cliente=cliente)

    # Cria os itens em OrdemServicoItem (lista)
    items = data.get('ordem_servico_itens')
    for item in items:
        servico_id = item.get('servico_id')
        servico = get_object_or_404(Servico, pk=servico_id)

        valor = item.get('valor')

        proxima_visita = item.get('proxima_visita')

        OrdemServicoItem.objects.create(
            ordem_servico=ordem_servico,
            servico=servico,
            valor=valor,
            proxima_visita=proxima_visita,
        )

    return {
        'ordem_servico_id': ordem_servico.pk,
        'status': HTTPStatus.CREATED
    }
