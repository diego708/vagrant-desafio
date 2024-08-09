from django import forms
from .models import Cargo, Cliente, Funcionario, Projeto


class CargoForm(forms.ModelForm):

    class Meta:
        model = Cargo
        fields = ('nome',)
        

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nome', 'cnpj',)


class FuncionarioForm(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        fields = ('nome', 'cpf', 'codigo', 'cargo',)


class ProjetoForm(forms.ModelForm):
    
    class Meta:
        model = Projeto
        fields = ('nome', 'descricao', 'status', 'cliente',)

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
