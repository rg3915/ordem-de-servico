from django.contrib import admin

from .models import OrdemServico, OrdemServicoItem, Servico


class OrdemServicoItemInline(admin.TabularInline):
    model = OrdemServicoItem
    extra = 0


@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    inlines = (OrdemServicoItemInline,)
    list_display = ('__str__', 'cliente', 'situacao')
    list_display_links = ('cliente',)
    search_fields = ('cliente__razao_social',)
    list_filter = ('situacao',)


admin.site.register(Servico)
