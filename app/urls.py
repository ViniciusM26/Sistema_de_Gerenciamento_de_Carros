"""
Configuração de URLs para o projeto Django.

A lista `urlpatterns` define as rotas do projeto, associando URLs a views específicas.
Mais informações: https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import path  # Importa a função path para definir rotas
from django.conf import settings  # Importa as configurações do projeto
from django.conf.urls.static import static  # Importa a função para servir arquivos estáticos

# Importa as views do app 'cars' para manipulação de carros
from cars.views import CarListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView  

# Importa as views do app 'accounts' para autenticação de usuários
from accounts.views import register_view, login_view, logout_view  

# Lista de URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a área administrativa do Django
    path('register/', register_view, name='register'),  # Rota para a página de registro de usuários
    path('login/', login_view, name='login'),  # Rota para a página de login
    path('logout/', logout_view, name='logout'),  # Rota para logout

    # Rotas relacionadas ao gerenciamento de carros
    path('cars/', CarListView.as_view(), name='cars_list'),  # Lista os carros cadastrados
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),  # Formulário para adicionar um novo carro
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),  # Exibe os detalhes de um carro específico
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),  # Atualiza os dados de um carro
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),  # Exclui um carro do banco de dados
] 

# Adiciona suporte a arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
