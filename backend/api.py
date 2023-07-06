from ninja import NinjaAPI

from backend.crm.crm_api import router as crm_router
from backend.servico.servico_api import router as servico_router

api = NinjaAPI(csrf=True)

api.add_router('/crm/', crm_router)
api.add_router('/servico/', servico_router)
