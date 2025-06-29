from django.urls import path
from clients.views import client_list_view, client_detail_view, client_create_view, client_delete_view, client_update_view


urlpatterns =  [

    path('clients/', client_list_view, name='clients-list'),
    path('clients/detail/<int:pk>', client_detail_view, name='clients-detail'),
    path('clients/create/', client_create_view, name='clients-create'),
    path('clients/update/<int:pk>', client_update_view, name='clients-update'),
    path('clients/delete/<int:pk>', client_delete_view, name='clients-delete'),
]