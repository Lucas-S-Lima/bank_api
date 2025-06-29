from django.contrib import admin
from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    
    list_display = ('origin_account', 'destination_account', 'cash', 'date')
    search_fields = ('origin_account', 'destination_account')
