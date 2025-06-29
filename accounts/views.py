from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from accounts.models import Account


def account_list_view(request):

    accounts = Account.objects.all()
    
    data = [{
        'client_id': accounts.client_id,
        'account_number': accounts.account_number,
        'bank': accounts.bank,
        'agency': accounts.agency,
        'account_type': accounts.account_type,
        'balance': accounts.balance
        
        } for account in accounts]

    return JsonResponse(data, safe=False)


def account_detail_view(request, pk):

    account = get_object_or_404(Account, pk=pk)

    data = {
        'client_id': account.client_id,
        'account_number': account.account_number,
        'bank': account.bank,
        'agency': account.agency,
        'account_type': account.account_type,
        'balance': account.balance
        
        } 

    return JsonResponse(data)


def account_create_view(request):

    client_id = request.POST.get('client_id')
    account_number = request.POST.get('account_number')
    bank = request.POST.get('bank')
    agency = request.POST.get('agency')
    account_type = request.POST.get('account_type')
    balance = request.POST.get('balance')

    new_account = Account(
        client_id=client_id,
        account_number=account_number, 
        bank=bank, 
        agency=agency,
        account_type=account_type,
        balance=balance,
        )
    
    new_account.save()

    return HttpResponse(status=201)


def account_update_view(request, pk):

    account = Account.objects.get(pk=pk)

    client_id = request.POST.get('client_id')
    account_number = request.POST.get('account_number')
    bank = request.POST.get('bank')
    agency = request.POST.get('agency')
    account_type = request.POST.get('account_type')
    balance = request.POST.get('balance')

    if client_id:
        account.client_id = client_id
    if account_number:
        account.account_number = account_number 
    if bank:
        account.bank = bank 
    if agency:
        account.agency = agency
    if account_type:
        account.account_type = account_type
    if balance:
        account.balance = balance

    account.save()

    return HttpResponse(status=200)


def account_delete_view(request, pk):

    account = Account.objects.get(pk=pk)

    account.delete()

    return HttpResponse(status=200)