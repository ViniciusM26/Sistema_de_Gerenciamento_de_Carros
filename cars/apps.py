from django.apps import AppConfig

class CarsConfig(AppConfig):
    """
    Configuração do aplicativo 'cars' dentro do projeto Django.

    Essa classe define configurações específicas para o aplicativo, incluindo
    a configuração do campo padrão para chaves primárias e a importação de sinais
    ao iniciar o aplicativo.
    """

    # Define o tipo padrão de campo de chave primária para os modelos do app
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome do aplicativo dentro do projeto Django
    name = 'cars'

    def ready(self):
        """
        Método chamado quando o aplicativo é carregado. 
        Aqui, os sinais do aplicativo 'cars' são importados para garantir
        que eles sejam registrados corretamente e possam ser utilizados
        ao longo do projeto.
        """
        import cars.signals
