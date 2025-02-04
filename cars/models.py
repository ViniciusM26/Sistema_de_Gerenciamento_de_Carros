from django.db import models  # Importa os modelos do Django para definir as tabelas do banco de dados

# Modelo que representa uma marca de carro
class Brand(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de ID gerado automaticamente (chave primária)
    name = models.CharField(max_length=200)  # Nome da marca com limite de 200 caracteres

    def __str__(self):  # Define a representação textual do objeto
        return self.name  # Retorna o nome da marca ao invés de "Brand Object"

# Modelo que representa um carro
class Car(models.Model):
    id = models.AutoField(primary_key=True)  # ID único para cada carro, gerado automaticamente
    model = models.CharField(max_length=200)  # Nome do modelo do carro
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') 
    # Relacionamento com a marca do carro (cada carro pertence a uma marca)   
    factory_year = models.IntegerField(blank=True, null=True)  # Ano de fabricação (opcional)
    model_year = models.IntegerField(blank=True, null=True)  # Ano do modelo (opcional)
    plate = models.CharField(max_length=10, blank=True, null=True)  # Placa do carro (opcional)
    value = models.FloatField(blank=True, null=True)  # Valor do carro (opcional)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)  
    # Campo para armazenar uma imagem do carro (opcional), salva na pasta 'cars/'

    def __str__(self):  # Define a representação textual do objeto
        return self.model  # Retorna o modelo do carro ao invés de "Car Object"
