from django.urls import path
from accounts.views import account_list_view, account_detail_view, account_create_view, account_update_view, account_delete_view


urlpatterns =  [

    path('accounts/', account_list_view, name='accounts-list'),
    path('accounts/detail/<int:pk>', account_detail_view, name='accounts-detail'),
    path('accounts/create/', account_create_view, name='accounts-create'),
    path('accounts/update/<int:pk>', account_update_view, name='accounts-update'),
    path('accounts/delete/<int:pk>', account_delete_view, name='accounts-delete'),
]