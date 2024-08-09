from django import forms
from .models import Atividade

class AtividadeForm(forms.ModelForm):

    class Meta:
        model = Atividade
        fields = ('nome', 'descricao', 'status', 'responsavel', 'projeto',)

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
