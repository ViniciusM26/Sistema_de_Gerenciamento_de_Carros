### 🚗 Sistema de Gerenciamento e Revenda de Carros

Bem-vindo ao Sistema de Gerenciamento e Revenda de Carros, um projeto desenvolvido em Django que facilita a administração e revenda de veículos. Este sistema inclui funcionalidades de cadastro, edição, exclusão e visualização detalhada de carros, além de integração com IA para gerar descrições automáticas dos veículos.

### 📌 Principais Funcionalidades

✅ Gerenciamento de carros (CRUD completo)

✅ Busca e listagem de veículos com exibição detalhada

✅ Autenticação de usuários e painel administrativo

✅ Upload de imagens para os veículos

✅ Integração com IA para gerar automaticamente descrições dos carros (API Gemini)

✅ Banco de Dados PostgreSQL para melhor escalabilidade

### 🏗️ Tecnologias Utilizadas:

🔹 Linguagem: Python 3.11.2

🔹 Framework: Django

🔹 Banco de Dados: PostgreSQL

🔹 Bibliotecas:

    ✅ Django - Framework principal
    
    ✅ Pillow - Para manipulação de imagens
    
    ✅ psycopg2 - Conexão com PostgreSQL
    
    ✅ google-generativeai - API da Gemini para IA

🚀 Como Instalar e Configurar o Projeto:

### 1️⃣ Clone o Repositório

``` 
git clone https://github.com/ViniciusM26/Cars.git
```

``` 
cd seu-repositorio
```

### 2️⃣ Crie e Ative o Ambiente Virtual

```
python -m venv venv 
```

``` 
source venv/bin/activate
```

No Windows:  
``` 
venv\Scripts\activate
```

### 3️⃣ Instale as Dependências

``` 
pip install -r requirements.txt
```

### 4️⃣ Configure as Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis (baseado no .env.example):

```
DATABASE_NAME=cars

DATABASE_USER=seu_usuario

DATABASE_PASSWORD=sua_senha

DATABASE_HOST=localhost

DATABASE_PORT=5432

GEMINI_API_KEY=sua_chave_aqui
```

🔴 Importante: Nunca compartilhe seu arquivo .env publicamente!

### 5️⃣ Configure o Banco de Dados

Certifique-se de que o PostgreSQL está instalado e rodando. Em seguida, aplique as migrações:

``` 
python manage.py migrate
```

Se desejar, crie um superusuário para acessar o painel administrativo:

``` 
python manage.py createsuperuser
```

### 6️⃣ Inicie o Servidor

``` 
python manage.py runserver
```

Agora, acesse ``` http://127.0.0.1:8000/ ``` no navegador para visualizar o sistema.

### 🧠 Integração com IA - Google Gemini

O sistema conta com integração de IA para gerar descrições automáticas dos carros.

🔹 Como funciona?

1️⃣ Ao cadastrar um carro sem bio, o sistema gera automaticamente uma descrição usando a API Gemini.

2️⃣ A IA recebe o modelo, marca e ano do carro e retorna um texto otimizado para revenda.

3️⃣ Se a chave da API não estiver configurada corretamente, uma bio padrão será usada.

🔹 Como configurar a API?

1️⃣ Obtenha uma chave de API no Google AI Studio:

``` 
https://aistudio.google.com/apikey
```

2️⃣ Adicione a chave no seu arquivo .env:

GEMINI_API_KEY=sua_chave_aqui

### 🔥 Possíveis Melhorias:

📌 Melhorar UI/UX dos templates

📌 Implementar testes automatizados

📌 Criar um sistema de relatórios e estatísticas


