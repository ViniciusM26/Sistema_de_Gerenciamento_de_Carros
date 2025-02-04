from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar páginas
from cars.models import Car  # Importa o modelo Car, que representa os carros no banco de dados
from cars.forms import CarModelForm  # Importa o formulário baseado no modelo Car

# View responsável por listar os carros cadastrados
def cars_views(request):
    # Busca todos os carros no banco de dados e ordena pelo modelo
    cars = Car.objects.all().order_by('model')
    
    # Obtém o termo de busca enviado pela URL (caso exista)
    search = request.GET.get('search')

    # Se houver um termo de busca, filtra os carros que contêm esse termo no modelo
    if search:
        cars = Car.objects.filter(model__icontains=search)

    # Renderiza a página 'cars.html' passando a lista de carros como contexto
    return render(
        request,
        'cars.html',
        {'cars': cars}
    )

# View responsável por adicionar um novo carro
def new_car_view(request):
    # Verifica se o formulário foi enviado via POST
    if request.method == 'POST':
        # Preenche o formulário com os dados enviados pelo usuário
        new_car_form = CarModelForm(request.POST, request.FILES)
        
        # Verifica se os dados do formulário são válidos
        if new_car_form.is_valid():
            # Salva o novo carro no banco de dados
            new_car_form.save()
            # Redireciona para a lista de carros após o cadastro
            return redirect('cars_list')

    else:
        # Se for uma requisição GET, apenas cria um formulário vazio
        new_car_form = CarModelForm()

    # Renderiza a página 'new_car.html', passando o formulário como contexto
    return render(
        request, 
        'new_car.html', 
        {'new_car_form': new_car_form}
    )
