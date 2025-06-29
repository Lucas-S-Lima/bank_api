from django.db import models
from clients.models import Client


class Account(models.Model):
    
    TIPO_DE_CONTA = {
        'CC': 'Conta Corrente',
        'CP': 'Conta Poupança',
        'CS': 'Conta Salário',
        'CCJ': 'Conta Conjunta',
    }


    client_id = models.ForeignKey(Client, max_length=120, verbose_name='Cliente', on_delete=models.PROTECT, related_name='client_account')
    account_number = models.CharField(max_length=30, verbose_name='Número da conta', unique=True)
    bank = models.CharField(max_length=50, verbose_name='Banco')
    agency = models.CharField(max_length=30, verbose_name='Agência')
    account_type = models.CharField(choices=TIPO_DE_CONTA, verbose_name='Tipo de conta')
    balance = models.FloatField(verbose_name='Saldo')

    def __str__(self):
        return self.account_number
