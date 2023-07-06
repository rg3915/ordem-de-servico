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
