from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('clients.urls')),
    path('api/v1/', include('accounts.urls')),
    path('ap1/v1/', include('transactions.urls')),
]
