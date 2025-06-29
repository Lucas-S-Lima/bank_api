from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from transactions.models import Transaction


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
    destination_accoount = request.POST.get('destination_account')
    cash = request.POST.get('cash')
    date = request.POST.get('date')

    new_transaction = Transaction(
        origin_account=origin_account,
        destination_accoount=destination_accoount, 
        cash=cash, 
        date=date
        )

    new_transaction.save()

    return HttpResponse(status=201)


def transaction_update_view(request, pk):

    transaction = Transaction.objects.get(pk=pk)

    origin_account = request.POST.get('origin_account')
    destination_account = request.POST.get('destination_account')
    cash = request.POST.get('cash')
    date = request.POST.get('date')

    if origin_account:
        transaction.origin_account = origin_account
    if destination_account:
        transaction.destination_account = destination_account
    if cash:
        transaction.cash = cash 
    if date:
        transaction.date = date

    transaction.save()

    return HttpResponse(status=200)


def transanction_delete_view(request, pk):

    transaction = Transaction.objects.get(pk=pk)

    transaction.delete()

    return HttpResponse(status=200)