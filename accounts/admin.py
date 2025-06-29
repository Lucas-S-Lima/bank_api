from django.contrib import admin
from accounts.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    
    list_display = ('client_id', 'account_number', 'bank', 'account_type', 'balance')
    search_fields = ('client_id', 'account_number')