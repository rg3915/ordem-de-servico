from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'bairro', 'cidade')
    search_fields = ('razao_social', 'bairro', 'cidade')
