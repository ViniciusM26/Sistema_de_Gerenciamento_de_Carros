from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
import google.generativeai as genai 
import os

# Configuração da API Gemini (segura via variável de ambiente)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Defina essa variável no .env ou no ambiente do servidor

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    raise ValueError("A chave da API Gemini não foi configurada corretamente.")

def get_car_ai_bio(model, brand, year):
    """
    Gera uma descrição automática para um carro usando IA Gemini.
    
    Parâmetros:
    - model (str): Modelo do carro
    - brand (str): Marca do carro
    - year (int): Ano do carro

    Retorna:
    - (str) Bio gerada pela IA
    """
    prompt = f"Crie uma descrição de venda para o carro {brand} {model} {year} com até 250 caracteres. Destaque características técnicas e benefícios desse modelo."

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Escolhendo o modelo Gemini
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else "Bio gerada automaticamente!"
    except Exception as e:
        print(f"Erro ao gerar bio com Gemini: {e}")
        return "Bio gerada automaticamente!"

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    """
    Antes de salvar um carro, verifica se o campo 'bio' está vazio.
    Se estiver, gera automaticamente uma descrição usando a IA Gemini.
    """
    if not instance.bio:
        instance.bio = get_car_ai_bio(instance.model, instance.brand, instance.model_year)

def car_inventory_update():
    """
    Atualiza o inventário de carros no sistema.

    Calcula a quantidade total de carros cadastrados e o valor total dos veículos
    e atualiza a tabela CarInventory com essas informações.
    """
    cars_count = Car.objects.all().count()  # Conta o número total de carros cadastrados
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']  # Soma os valores de todos os carros
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )  # Cria um novo registro no inventário com os valores atualizados


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    """
    Sinal acionado após a criação ou atualização de um objeto Car.

    Sempre que um carro for salvo no banco de dados, a função car_inventory_update()
    será chamada para atualizar o inventário de carros.
    """
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    """
    Sinal acionado após a exclusão de um objeto Car.

    Quando um carro for deletado, a função car_inventory_update() será executada
    para manter os dados do inventário atualizados.
    """
    car_inventory_update()
