from django.urls import path
from .views import *

urlpatterns = [
    path('', accounts_list, name='accounts_list'),
    path('add/', account_create, name='account_create'),
    path('update/<int:id>/', account_update, name='account_update'),
    path('delete/<int:id>/', account_delete, name='account_delete'),
    path('info/<int:id>/', account_info, name='account_info'),
]
m