from django.urls import path, include
from website.views import index, sobre, login, cadastrar_ideia, remover_ideias

urlpatterns = [
    path('', index),
    path('sobre', sobre),
    path('login', login),
    path('ideias', cadastrar_ideia),
    path('remover_ideias/<int:id>', remover_ideias)
]
