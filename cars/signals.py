from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory

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

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    """
    Sinal acionado antes de salvar um objeto Car.

    Se o campo 'bio' do carro estiver vazio, ele é preenchido automaticamente
    com uma mensagem padrão. No futuro, pode ser integrado com uma IA (como Gemini
    ou um modelo local via Ollama) para gerar uma bio personalizada.
    """
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente!'

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
