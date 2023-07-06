from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI

from .api import api

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('crm/', include('backend.crm.urls', namespace='crm')),
    path('servico/', include('backend.servico.urls', namespace='servico')),
    path('admin/', admin.site.urls),
    path("api/v1/", api.urls),
]
