from django.urls import path
from . import views

urlpatterns = [
    path('gerenciamento/', views.gerenciamento, name='gerenciamento'),
    path('gerenciamento_projeto/', views.gerenciamento_projeto, name='gerenciamento_projeto'),
    path('testing_atividade/', views.testing_atividade, name='testing_atividade'),
    path('gerenciamento_projeto_editar/<int:pk>/', views.gerenciamento_projeto_editar, name='gerenciamento_projeto_editar'),
    path('gerenciamento_projeto_excluir/<int:pk>/', views.gerenciamento_projeto_excluir, name='gerenciamento_projeto_excluir'),
    path('gerenciamento_projeto_excluir_item/<int:pk>/', views.gerenciamento_projeto_excluir_item, name='gerenciamento_projeto_excluir_item'),
]
