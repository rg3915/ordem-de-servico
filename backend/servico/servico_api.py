from typing import List
from ninja import Router
from ninja.orm import create_schema

from backend.servico.models import Servico

router = Router()

ServicoSchema = create_schema(Servico, fields=(
    'id',
    'titulo',
))


@router.get('servico/', response=List[ServicoSchema])
def list_servico(request, search=None):
    if search:
        return Servico.objects.filter(titulo__istartswith=search)
    return Servico.objects.all()
