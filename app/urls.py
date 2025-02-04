"""
Configuração de URLs para o projeto Django.

A lista `urlpatterns` define as rotas do projeto, associando URLs a views específicas.
Mais informações: https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import path  # Importa a função path para definir rotas
from django.conf import settings  # Importa as configurações do projeto
from django.conf.urls.static import static  # Importa a função para servir arquivos estáticos
from cars.views import cars_views, new_car_view # Importa as views do app 'cars' 
from accounts.views import register_view, login_view, logout_view # Importa as views do app 'accounts'  

# Lista de URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a área administrativa do Django
    path('register/', register_view, name='register'),  # Rota para a página de registro
    path('login/', login_view, name='login'),  # Rota para a página de login
    path('logout/', logout_view, name='logout'),  # Rota para logout
    path('cars/', cars_views, name='cars_list'),  # Rota para listar os carros
    path('new_car/', new_car_view, name='new_car'),  # Rota para adicionar um novo carro
] 

# Adiciona suporte a arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
