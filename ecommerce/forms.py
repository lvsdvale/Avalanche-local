from django import forms
from .models import itemcarrinho
itemcarrinhoformset = forms.modelformset_factory(itemcarrinho,fields=['quantidade'],can_delete=True,extra=0)


