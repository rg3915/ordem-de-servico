from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .forms import ClienteForm
from .models import Cliente


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 20

    def get_queryset(self):
        qs = self.model.objects.all()
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(
                Q(razao_social__icontains=search)
                | Q(bairro__icontains=search)
                | Q(cidade__icontains=search)
            )
        return qs


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm


# class ClienteDeleteView(DeleteView):
#     model = Cliente
#     success_url = reverse_lazy('crm:cliente_list')
