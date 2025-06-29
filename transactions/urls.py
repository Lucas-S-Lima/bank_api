from django.urls import path
from transactions.views import transaction_list_view, transaction_detail_view, transaction_create_view, transaction_update_view, transanction_delete_view


urlpatterns =  [

    path('transactions/', transaction_list_view, name='transactions-list'),
    path('transactions/detail/<int:pk>', transaction_detail_view, name='transactions-detail'),
    path('transactions/create/', transaction_create_view, name='transactions-create'),
    path('transactions/update/<int:pk>', transaction_update_view, name='transactions-update'),
    path('transactions/delete/<int:pk>', transanction_delete_view, name='transactions-delete'),
]