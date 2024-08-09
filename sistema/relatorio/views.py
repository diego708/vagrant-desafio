from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from projeto.models import Atividade
from cadastro.models import Projeto, Cliente, Funcionario

def relatorio(request):
    template = loader.get_template('relatorio/index.html')

    data = {
        "projetos_finalizados": [],
        "projetos_andamento": []
    }

    data_projeto = Projeto.objects.all().values()

    if data_projeto:
        for projeto in data_projeto:
            data_dict = {
                'projeto_nome': projeto['nome'],
                'cliente_nome': '',
                'atividade': [],
            }

            cliente = Cliente.objects.filter(id=projeto['cliente_id']).values()
            if cliente:
                data_dict['cliente_nome'] = cliente[0]['nome']

            atividade = Atividade.objects.filter(projeto=projeto['id']).values()
            if atividade:
                for item in atividade:
                    atividade_dict = {
                        'atividade_nome': item['nome'],
                        'responsavel_nome': '',
                        'status': 'Em Andamento',
                    }

                    if item['status']:
                        atividade_dict['status'] = 'Finalizado'

                    responsavel = Funcionario.objects.filter(id=item['responsavel_id']).values()
                    if responsavel:
                        atividade_dict['responsavel_nome'] = responsavel[0]['nome']

                    data_dict['atividade'].append(atividade_dict)
            
            if projeto['status']:
                data['projetos_finalizados'].append(data_dict)
            else:
                data['projetos_andamento'].append(data_dict)

    context = {'data': data,}
    
    return HttpResponse(template.render(context, request))
