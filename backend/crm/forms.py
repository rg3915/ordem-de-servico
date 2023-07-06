from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    cnpj = forms.CharField(max_length=18, label='CNPJ')

    class Meta:
        model = Cliente
        fields = ('razao_social', 'cnpj', 'endereco', 'complemento', 'bairro', 'cidade', 'uf', 'cep')
