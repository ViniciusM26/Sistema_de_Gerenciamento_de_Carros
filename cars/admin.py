from django.contrib import admin  # Importa o módulo de administração do Django
from cars.models import Car, Brand  # Importa os modelos Car e Brand

# Configuração do painel administrativo para a marca de carros (Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Exibe o campo 'name' na listagem do admin
    search_fields = ('name',)  # Adiciona um campo de busca pelo nome da marca

# Registra o modelo Brand no painel administrativo com as configurações definidas
admin.site.register(Brand, BrandAdmin)

# Configuração do painel administrativo para os carros (Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')  
    # Define os campos que serão exibidos na tabela do painel admin
    
    search_fields = ('model', 'brand')  
    # Adiciona um campo de busca pelo modelo e marca do carro

# Registra o modelo Car no painel administrativo com as configurações definidas
admin.site.register(Car, CarAdmin)
