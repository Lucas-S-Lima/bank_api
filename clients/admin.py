from django.contrib import admin
from clients.models import Client


@admin.register(Client)

class ClienttAdmin(admin.ModelAdmin):
    list_display = ('name', 'register_number', 'email', 'password')
    search_fields = ('name', 'register_number')