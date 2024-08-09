from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Cargo, Cliente, Funcionario, Projeto

from .forms import CargoForm, ClienteForm, FuncionarioForm, ProjetoForm


def cadastro(request):
   template = loader.get_template('cadastro/index.html')
   
   return HttpResponse(template.render())


def cargo(request):
    cargo_data = Cargo.objects.all().values()
    template = loader.get_template('cadastro/cargo.html')

    context = {'data': cargo_data,}
    
    return HttpResponse(template.render(context, request))


def testing_cargo(request):
  template = loader.get_template('cadastro/cargo.html')
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


def cargo_detalhe(request):
   if request.method == 'POST':
      form = CargoForm(request.POST)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('cadastro/salvar.html')
         return HttpResponse(template.render())
   
   form = CargoForm()
   template = loader.get_template('cadastro/cargo_detalhe.html')

   return HttpResponse(template.render({'form': form}, request))


def cargo_editar(request, pk):
   post = get_object_or_404(Cargo, pk=pk)

   if request.method == "POST":
      form = CargoForm(request.POST, instance=post)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('cadastro/salvar.html')
         return HttpResponse(template.render())

   form = CargoForm(instance=post)
   template = loader.get_template('cadastro/cargo_detalhe.html')

   return HttpResponse(template.render({'form': form}, request))
   

def cargo_excluir_item(request, pk=None):
   data = get_object_or_404(Cargo, pk=pk)

   context ={
      'data': data
   }
   
   template = loader.get_template('cadastro/cargo_excluir.html')
   
   return HttpResponse(template.render(context, request))


def cargo_excluir(request, pk=None):
   data = get_object_or_404(Cargo, pk=pk)
   
   if data:
      data.delete()

      template = loader.get_template('cadastro/excluir.html')
      return HttpResponse(template.render())
   
   form = CargoForm()
   template = loader.get_template('cadastro/index.html')

   return HttpResponse(template.render({'form': form}, request))


def cliente(request):
    cliente_data = Cliente.objects.all().values()
    template = loader.get_template('cadastro/cliente.html')

    context = {'data': cliente_data,}
    
    return HttpResponse(template.render(context, request))


def testing_cliente(request):
  template = loader.get_template('cadastro/cliente.html')
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


def cliente_detalhe(request):
   if request.method == 'POST':
      form = ClienteForm(request.POST)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('cadastro/salvar.html')
         return HttpResponse(template.render())
   
   form = ClienteForm()
   template = loader.get_template('cadastro/cliente_detalhe.html')

   return HttpResponse(template.render({'form': form}, request))


def cliente_editar(request, pk):
   post = get_object_or_404(Cliente, pk=pk)

   if request.method == "POST":
      form = ClienteForm(request.POST, instance=post)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('cadastro/salvar.html')
         return HttpResponse(template.render())

   form = ClienteForm(instance=post)
   template = loader.get_template('cadastro/cliente_detalhe.html')

   return HttpResponse(template.render({'form': form}, request))


def cliente_excluir_item(request, pk=None):
   data = get_object_or_404(Cliente, pk=pk)

   context ={
      'data': data
   }
   
   template = loader.get_template('cadastro/cliente_excluir.html')
   
   return HttpResponse(template.render(context, request))


def cliente_excluir(request, pk=None):
   data = get_object_or_404(Cliente, pk=pk)
   
   if data:
      data.delete()

      template = loader.get_template('cadastro/excluir.html')
      return HttpResponse(template.render())
   
   form = ClienteForm()
   template = loader.get_template('cadastro/index.html')

   return HttpResponse(template.render({'form': form}, request))


def funcionario(request):
    funcionario_data = Funcionario.objects.all().values()
    template = loader.get_template('cadastro/funcionario.html')

    context = {'data': funcionario_data,}
    
    return HttpResponse(template.render(context, request))


def testing_funcionario(request):
  template = loader.get_template('cadastro/funcionario.html')
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

def funcionario_detalhe(request):
   if request.method == 'POST':
      form = FuncionarioForm(request.POST)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('cadastro/salvar.html')
         return HttpResponse(template.render())
   
   form = FuncionarioForm()
   template = loader.get_template('cadastro/funcionario_detalhe.html')

   return HttpResponse(template.render({'form': form}, request))


def funcionario_editar(request, pk):
   post = get_object_or_404(Funcionario, pk=pk)

   if request.method == "POST":
      form = FuncionarioForm(request.POST, instance=post)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('cadastro/salvar.html')
         return HttpResponse(template.render())

   form = FuncionarioForm(instance=post)
   template = loader.get_template('cadastro/funcionario_detalhe.html')

   return HttpResponse(template.render({'form': form}, request))


def funcionario_excluir_item(request, pk=None):
   data = get_object_or_404(Funcionario, pk=pk)

   context ={
      'data': data
   }
   
   template = loader.get_template('cadastro/funcionario_excluir.html')
   
   return HttpResponse(template.render(context, request))


def funcionario_excluir(request, pk=None):
   data = get_object_or_404(Funcionario, pk=pk)
   
   if data:
      data.delete()

      template = loader.get_template('cadastro/excluir.html')
      return HttpResponse(template.render())
   
   form = FuncionarioForm()
   template = loader.get_template('cadastro/index.html')

   return HttpResponse(template.render({'form': form}, request))


def projeto(request):
    projeto_data = Projeto.objects.all().values()
    template = loader.get_template('cadastro/projeto.html')

    context = {'data': projeto_data,}
    
    return HttpResponse(template.render(context, request))


def testing_projeto(request):
  template = loader.get_template('cadastro/projeto.html')
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

def projeto_detalhe(request):
   if request.method == 'POST':
      form = ProjetoForm(request.POST)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('cadastro/salvar.html')
         return HttpResponse(template.render())
   
   form = ProjetoForm()
   template = loader.get_template('cadastro/projeto_detalhe.html')

   return HttpResponse(template.render({'form': form}, request))


def projeto_editar(request, pk):
   post = get_object_or_404(Projeto, pk=pk)

   if request.method == "POST":
      form = ProjetoForm(request.POST, instance=post)

      if form.is_valid():
         post = form.save(commit=False)
         post.save()

         template = loader.get_template('cadastro/salvar.html')
         return HttpResponse(template.render())

   form = ProjetoForm(instance=post)
   template = loader.get_template('cadastro/projeto_detalhe.html')

   return HttpResponse(template.render({'form': form}, request))


def projeto_excluir_item(request, pk=None):
   data = get_object_or_404(Projeto, pk=pk)

   context ={
      'data': data
   }
   
   template = loader.get_template('cadastro/projeto_excluir.html')
   
   return HttpResponse(template.render(context, request))


def projeto_excluir(request, pk=None):
   data = get_object_or_404(Projeto, pk=pk)
   
   if data:
      data.delete()

      template = loader.get_template('cadastro/excluir.html')
      return HttpResponse(template.render())
   
   form = ProjetoForm()
   template = loader.get_template('cadastro/index.html')

   return HttpResponse(template.render({'form': form}, request))
