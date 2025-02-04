from django import forms  # Importa o módulo de formulários do Django
from cars.models import Car  # Importa o modelo Car para criar um formulário baseado nele

# Formulário baseado no modelo Car
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car  # Define o modelo associado ao formulário
        fields = '__all__'  # Inclui todos os campos do modelo no formulário

    # Validação personalizada para o campo 'value' (valor do carro)
    def clean_value(self):
        value = self.cleaned_data.get('value')  # Obtém o valor inserido no formulário

        # Verifica se o valor do carro é menor que 20.000
        if value < 20000:
            self.add_error('value', 'Valor mínimo é de R$ 20.000')  # Adiciona um erro ao campo

        return value  # Retorna o valor validado

    # Validação personalizada para o campo 'factory_year' (ano de fabricação)
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')  # Obtém o ano de fabricação inserido

        # Verifica se o ano de fabricação é menor que 1975
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975')  
            # Adiciona um erro ao campo

        return factory_year  # Retorna o ano de fabricação validado
