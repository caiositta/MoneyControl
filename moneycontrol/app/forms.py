from django import forms
from .models import Despesas

class DespesasForm(forms.ModelForm):
    class Meta:
        model = Despesas
        fields = ['nome','empresa','data_vencimento','data_pagamento','valor']