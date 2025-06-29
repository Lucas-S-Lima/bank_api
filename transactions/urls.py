from django.urls import path
from transactions.views import transaction_list_view, transaction_detail_view, transaction_create_view


urlpatterns =  [

    path('transactions/', transaction_list_view, name='transactions-list'),
    path('transactions/detail/<int:pk>', transaction_detail_view, name='transactions-detail'),
    path('transactions/create/', transaction_create_view, name='transactions-create'),
]