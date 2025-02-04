from django.shortcuts import render, redirect  # Importa funções para renderizar páginas e redirecionar usuários
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Formulários padrão do Django para autenticação
from django.contrib.auth import authenticate, login, logout  # Funções para autenticação e gerenciamento de login/logout

# View para registrar um novo usuário
def register_view(request):

    if request.method == "POST":  # Se o formulário for enviado
        user_form = UserCreationForm(request.POST)  # Cria o formulário com os dados enviados

        if user_form.is_valid():  # Verifica se os dados são válidos
            user_form.save()  # Salva o novo usuário no banco de dados
            return redirect('login')  # Redireciona para a página de login após o cadastro
        
    else:
        user_form = UserCreationForm()  # Se for um acesso via GET, exibe o formulário vazio

    return render(
        request, 
        'register.html', 
        {'user_form': user_form}
    )  # Renderiza a página de registro com o formulário

# View para fazer login
def login_view(request):

    if request.method == 'POST':  # Se o formulário for enviado
        username = request.POST["username"]  # Obtém o nome de usuário do formulário
        password = request.POST["password"]  # Obtém a senha do formulário
        user = authenticate(request, username=username, password=password)  # Autentica o usuário

        if user is not None:  # Se o usuário for autenticado com sucesso
            login(request, user)  # Realiza o login
            return redirect('cars_list')  # Redireciona para a lista de carros
        else:
            login_form = AuthenticationForm()  # Exibe um formulário vazio em caso de erro

    else:
        login_form = AuthenticationForm()  # Se for um acesso via GET, exibe o formulário de login vazio

    return render(
        request, 
        'login.html', 
        {'login_form': login_form}
    )  # Renderiza a página de login com o formulário

# View para fazer logout
def logout_view(request):
    
    logout(request)  # Desconecta o usuário
    return redirect('cars_list')  # Redireciona para a lista de carros após o logout
