from typing import List

from ninja import Router
from ninja.orm import create_schema

from backend.crm.models import Cliente

router = Router()

ClienteSchema = create_schema(Cliente, fields=(
    'id',
    'razao_social',
    'endereco',
    'bairro',
))


@router.get('cliente/', response=List[ClienteSchema])
def list_cliente(request, search=None):
    if search:
        return Cliente.objects.filter(razao_social__istartswith=search)
    return Cliente.objects.all()
