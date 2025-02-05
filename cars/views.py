"""
Views do aplicativo 'cars'.

Este módulo contém as views baseadas em classes (Class-Based Views - CBV) para a listagem, criação, 
detalhamento, atualização e exclusão de carros cadastrados no sistema.
"""

from cars.models import Car  # Importa o modelo Car, que representa os carros no banco de dados
from cars.forms import CarModelForm  # Importa o formulário baseado no modelo Car
from django.urls import reverse_lazy  # Importa a função reverse_lazy para redirecionamento dinâmico
from django.contrib.auth.decorators import login_required  # Importa o decorador para exigir autenticação do usuário
from django.utils.decorators import method_decorator  # Permite aplicar decoradores em views baseadas em classes
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView  # Importa as classes genéricas de views

# View baseada em classe (CBV) para listar os carros cadastrados
class CarListView(ListView):
    model = Car  # Define o modelo que será utilizado na listagem
    template_name = 'cars.html'  # Especifica o template a ser renderizado
    context_object_name = 'cars'  # Nome da variável que será passada para o template

    def get_queryset(self):
        """
        Sobrescreve o método padrão para personalizar a busca de carros.
        Ordena os carros pelo nome do modelo e permite a busca por nome (case insensitive).
        """
        cars = super().get_queryset().order_by('model')  # Ordena os carros pelo campo 'model'
        search = self.request.GET.get('search')  # Obtém o termo de busca, se houver

        if search:
            cars = cars.filter(model__icontains=search)  # Filtra os carros que contêm o termo pesquisado no modelo
        return cars  # Retorna a lista de carros filtrada ou ordenada

# View baseada em classe (CBV) para exibir os detalhes de um carro específico
class CarDetailView(DetailView):
    model = Car  # Define o modelo que será utilizado na exibição dos detalhes
    template_name = 'car_detail.html'  # Especifica o template a ser renderizado

# View baseada em classe (CBV) para adicionar um novo carro (restrito a usuários autenticados)
@method_decorator(login_required(login_url='login'), name='dispatch')  # Exige autenticação para acessar esta view
class NewCarCreateView(CreateView):
    model = Car  # Define o modelo que será utilizado para criar um novo carro
    form_class = CarModelForm  # Utiliza o formulário baseado no modelo Car
    template_name = 'new_car.html'  # Especifica o template a ser renderizado
    success_url = '/cars/'  # Redireciona o usuário para a lista de carros após um cadastro bem-sucedido

# View baseada em classe (CBV) para atualizar um carro existente (restrito a usuários autenticados)
@method_decorator(login_required(login_url='login'), name='dispatch')  # Exige autenticação para acessar esta view
class CarUpdateView(UpdateView):
    model = Car  # Define o modelo que será utilizado para atualização
    form_class = CarModelForm  # Utiliza o formulário baseado no modelo Car
    template_name = 'car_update.html'  # Especifica o template a ser renderizado

    def get_success_url(self):
        """
        Define a URL de sucesso após a atualização de um carro.
        Redireciona para a página de detalhes do carro atualizado.
        """
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

# View baseada em classe (CBV) para excluir um carro existente (restrito a usuários autenticados)
@method_decorator(login_required(login_url='login'), name='dispatch')  # Exige autenticação para acessar esta view
class CarDeleteView(DeleteView):
    model = Car  # Define o modelo que será utilizado para exclusão
    template_name = 'car_delete.html'  # Especifica o template a ser renderizado
    success_url = '/cars/'  # Redireciona o usuário para a lista de carros após a exclusão
