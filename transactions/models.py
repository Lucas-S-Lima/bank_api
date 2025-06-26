from django.db import models
from accounts.models import Account


class Transaction(models.Model):

    origin_account = models.ForeignKey(Account, on_delete=models.PROTECT, verbose_name='Conta de origem', related_name='transactions_sent')
    destination_account = models.ForeignKey(Account, on_delete=models.PROTECT, verbose_name='Conta de destino', related_name='transactions_received')
    cash = models.FloatField(verbose_name='Valor')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Data')  

    def __str__(self):
        return f'{self.origin_account} -> {self.destination_account} - R$ {self.cash}'
    
