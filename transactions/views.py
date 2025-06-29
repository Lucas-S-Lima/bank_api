from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from transactions.models import Transaction
from accounts.models import Account


def transaction_list_view(request):

    transactions = Transaction.objects.all()
    
    data = [{
        'origin_account': transactions.origin_account,
        'destination_account': transactions.destination_account,
        'cash': transactions.cash,
        'date': transactions.date,
        
        } for transaction in transactions]

    return JsonResponse(data, safe=False)


def transaction_detail_view(request, pk):

    transaction = get_object_or_404(Transaction, pk=pk)

    data = {
        'origin_account': transaction.origin_account,
        'destination_account': transaction.destination_account,
        'cash': transaction.cash,
        'date': transaction.date,
        
        }

    return JsonResponse(data)


def transaction_create_view(request):

    origin_account = request.POST.get('origin_account')
    destination_account = request.POST.get('destination_account')
    cash = request.POST.get('cash')
    date = request.POST.get('date')

    new_transaction = Transaction(
        origin_account=origin_account,
        destination_accoount=destination_account, 
        cash=cash, 
        date=date
        )
    
    new_transaction.save()
    
    origin_account_instance = Account.objects.get(origin_account=origin_account)
    origin_account_instance.balance -= cash

    destination_account_instance = Account.objects.get(destination_account=destination_account)
    destination_account_instance.balance += cash

    origin_account_instance.save()
    destination_account_instance.save()
    
    return HttpResponse(status=201)



    
    




