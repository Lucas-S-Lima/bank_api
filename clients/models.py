from django.db import models


class Client(models.Model):

    name = models.CharField(max_length=120, verbose_name='Nome completo')
    register_number = models.CharField(max_length=18, verbose_name='CPF/CNPJ', unique=True)
    email = models.EmailField(max_length=50, verbose_name='E-mail', unique=True)
    password = models.CharField(max_length=100, verbose_name='Senha')

    def __str__(self):
        return self.name
