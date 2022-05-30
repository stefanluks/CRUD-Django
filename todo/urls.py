from django.contrib import admin
from django.urls import path, include
from .views import Home, Concluir, Excluir, CriarTarefa, CriarLista, CriarConta, ExcluirLista

urlpatterns = [
    path('', Home, name="home"),
    path('criarTarefa/', CriarTarefa, name="criarTarefa"),
    path('criarConta/', CriarConta, name="criarConta"),
    path('criarLista/', CriarLista, name="criarLista"),
    path('excluir/<int:id>', Excluir, name="excluir"),
    path('excluirLista/<int:id>', ExcluirLista, name="excluirLista"),
    path('concluir/<int:id>', Concluir, name="concluir"),
    path('desconcluir/<int:id>', Concluir, name="desconcluir"),
]
