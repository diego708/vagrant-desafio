from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cargo/', views.cargo, name='cargo'),
    path('cargo_detalhe/', views.cargo_detalhe, name='cargo_detalhe'),
    path('testing_cargo/', views.testing_cargo, name='testing_cargo'),
    path('cargo_editar/<int:pk>/', views.cargo_editar, name='cargo_editar'),
    path('cargo_excluir/<int:pk>/', views.cargo_excluir, name='cargo_excluir'),
    path('cargo_excluir_item/<int:pk>/', views.cargo_excluir_item, name='cargo_excluir_item'),
    path('cliente/', views.cliente, name='cliente'),
    path('cliente_detalhe/', views.cliente_detalhe, name='cliente_detalhe'),
    path('testing_cliente/', views.testing_cliente, name='testing_cliente'),
    path('cliente_editar/<int:pk>/', views.cliente_editar, name='cliente_editar'),
    path('cliente_excluir/<int:pk>/', views.cliente_excluir, name='cliente_excluir'),
    path('cliente_excluir_item/<int:pk>/', views.cliente_excluir_item, name='cliente_excluir_item'),
    path('funcionario/', views.funcionario, name='funcionario'),
    path('funcionario_detalhe/', views.funcionario_detalhe, name='funcionario_detalhe'),
    path('testing_funcionario/', views.testing_funcionario, name='testing_funcionario'),
    path('funcionario_editar/<int:pk>/', views.funcionario_editar, name='funcionario_editar'),
    path('funcionario_excluir/<int:pk>/', views.funcionario_excluir, name='funcionario_excluir'),
    path('funcionario_excluir_item/<int:pk>/', views.funcionario_excluir_item, name='funcionario_excluir_item'),
    path('projeto/', views.projeto, name='projeto'),
    path('projeto_detalhe/', views.projeto_detalhe, name='projeto_detalhe'),
    path('testing_projeto/', views.testing_projeto, name='testing_projeto'),
    path('projeto_editar/<int:pk>/', views.projeto_editar, name='projeto_editar'),
    path('projeto_excluir/<int:pk>/', views.projeto_excluir, name='projeto_excluir'),
    path('projeto_excluir_item/<int:pk>/', views.projeto_excluir_item, name='projeto_excluir_item'),
]
