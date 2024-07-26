from django.db import models
from. import models

class SevicosEfetuados(models.Model):
    nome_do_cliente = models.CharField(max_lenght=100)
    servico = models.CharField(max_lenght=100)
    valor_cobrado = models.IntgerField()
    pagamento = models.CharField(max_lenght=100)

        def __str__(self.nome_do_cliente):
            return self.nome_do_cliente
    
