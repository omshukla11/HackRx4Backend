from django.urls import path
from .views import BankAccountAPI, TransactionAPI, MessageTransactionsAPI

urlpatterns = [
    path('account/', BankAccountAPI.as_view(), name='Bank-Accounts'),
    path('transaction/', TransactionAPI.as_view(), name='Transactions'),
    path('transactionmessage/', MessageTransactionsAPI.as_view(), name='Transactions Messages'),
]