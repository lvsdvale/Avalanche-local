from django import forms
from .models import pagamentos
PagamentoDepositoForm = forms.modelformset_factory(pagamentos,fields=['image','deposito'],can_delete=True,extra=0)
PagamentoPicpayForm = forms.modelformset_factory(pagamentos,fields=['deposito'])