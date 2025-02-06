from django.db import models  # Importa os modelos do Django para definir as tabelas do banco de dados

# Modelo que representa uma marca de carro
class Brand(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de ID gerado automaticamente (chave primária)
    name = models.CharField(max_length=200)  # Nome da marca do carro, com limite de 200 caracteres

    def __str__(self):
        """
        Retorna a representação textual do objeto.
        Em vez de exibir "Brand Object", retorna o nome da marca para facilitar a identificação.
        """
        return self.name

# Modelo que representa um carro
class Car(models.Model):
    id = models.AutoField(primary_key=True)  # ID único para cada carro, gerado automaticamente
    model = models.CharField(max_length=200)  # Nome do modelo do carro
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='car_brand'
    )  # Relacionamento com a marca (um carro pertence a uma marca)
    factory_year = models.IntegerField(blank=True, null=True)  # Ano de fabricação do carro (opcional)
    model_year = models.IntegerField(blank=True, null=True)  # Ano do modelo do carro (opcional)
    plate = models.CharField(max_length=10, blank=True, null=True)  # Placa do carro (opcional)
    value = models.FloatField(blank=True, null=True)  # Valor do carro (opcional)
    photo = models.ImageField(
        upload_to='cars/', blank=True, null=True
    )  # Foto do carro (opcional), armazenada na pasta 'cars/'
    bio = models.TextField(blank=True, null=True)  # Campo opcional para descrição do carro

    def __str__(self):
        """
        Retorna a representação textual do objeto.
        Em vez de exibir "Car Object", retorna o nome do modelo do carro para facilitar a identificação.
        """
        return self.model

# Modelo que representa o inventário de carros cadastrados
class CarInventory(models.Model):
    cars_count = models.IntegerField()  # Quantidade total de carros cadastrados
    cars_value = models.FloatField()  # Soma dos valores de todos os carros cadastrados
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora da criação do registro no inventário

    class Meta:
        ordering = ['-created_at']  # Ordena os registros do inventário do mais recente para o mais antigo

    def __str__(self):
        """
        Retorna a representação textual do objeto.
        Exibe a quantidade total de carros e o valor total do inventário.
        """
        return f'{self.cars_count} - {self.cars_value}'
