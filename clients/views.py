from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from clients.models import Client


def client_list_view(request):

    clients = Client.objects.all()
    
    data = [{
        'name': client.name,
        'register_number': client.register_number,
        'email': client.email,
        'password': client.password,
        
        } for client in clients]

    return JsonResponse(data, safe=False)

def client_detail_view(request, pk):

    client = get_object_or_404(Client, pk=pk)

    data = {
        'name': client.name,
        'register_number': client.register_number,
        'email': client.email,
        'password': client.password
    }

    return JsonResponse(data)


def client_create_view(request):

    name = request.POST.get('name')
    register_number = request.POST.get('register_number')
    email = request.POST.get('email')
    password = request.POST.get('password')

    new_client = Client(
        name=name,
        register_number=register_number, 
        email=email, 
        password=password
        )

    new_client.save()

    return HttpResponse(status=201)


def client_update_view(request, pk):

    client = Client.objects.get(pk=pk)

    name = request.POST.get('name')
    register_number = request.POST.get('register_number')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if name:
        client.name = name
    if register_number:
        client.register_number = register_number 
    if email:
        client.email = email 
    if password:
        client.password = password 

    client.save()

    return HttpResponse(status=200)

def client_delete_view(request, pk):

    client = Client.objects.get(pk=pk)

    client.delete()

    return HttpResponse(status=200)
    
