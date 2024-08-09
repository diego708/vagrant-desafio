from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Atividade

from .forms import AtividadeForm


def gerenciamento(request):
    projeto_data = Atividade.objects.all().values()
    template = loader.get_template('projeto/index.html')

    context = {'data': projeto_data,}
    
    return HttpResponse(template.render(context, request))


def testing_atividade(request):
  template = loader.get_template('projeto/index.html')
  context = {
    'data': [
       { 'id': 152,
         'nome': 'Teste'
       },
       {
         'id': 166,
         'nome': 'Teste XX'
       },]   
  }
  return HttpResponse(template.render(context, request))


def gerenciamento_projeto(request):
   if request.method == 'POST':
      form = AtividadeForm(request.POST)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('projeto/salvar.html')
         return HttpResponse(template.render())
   
   form = AtividadeForm()
   template = loader.get_template('projeto/gerenciamento_projeto.html')

   return HttpResponse(template.render({'form': form}, request))


def gerenciamento_projeto_editar(request, pk):
   post = get_object_or_404(Atividade, pk=pk)

   if request.method == "POST":
      form = AtividadeForm(request.POST, instance=post)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('projeto/salvar.html')
         return HttpResponse(template.render())

   form = AtividadeForm(instance=post)
   template = loader.get_template('projeto/gerenciamento_projeto.html')

   return HttpResponse(template.render({'form': form}, request))

def gerenciamento_projeto_excluir_item(request, pk=None):
   data = get_object_or_404(Atividade, pk=pk)

   context ={
      'data': data
   }
   
   template = loader.get_template('projeto/gerenciamento_projeto_excluir.html')
   
   return HttpResponse(template.render(context, request))


def gerenciamento_projeto_excluir(request, pk=None):
   data = get_object_or_404(Atividade, pk=pk)
   
   if data:
      data.delete()

      template = loader.get_template('projeto/excluir.html')
      return HttpResponse(template.render())
   
   form = AtividadeForm()
   template = loader.get_template('projeto/index.html')

   return HttpResponse(template.render({'form': form}, request))
