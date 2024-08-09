from django.urls import path
from . import views

urlpatterns = [
    path('relatorio/', views.relatorio, name='relatorio'),
]
