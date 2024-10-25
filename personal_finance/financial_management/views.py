from personal_finance.repositories.account_repository import AccountRepository
from personal_finance.repositories.category_repository import CategoryRepository
from personal_finance.repositories.expense_repository import ExpenseRepository
from personal_finance.repositories.transaction_repository import TransactionRepository
from personal_finance.serializers.account_serializer import AccountSerializer
from personal_finance.serializers.category_serializer import CategorySerializer
from personal_finance.serializers.expense_serializer import ExpenseSerializer
from personal_finance.serializers.transaction_serializer import TransactionSerializer
from rest_framework import viewsets

category_respository = CategoryRepository()
transaction_respository = TransactionRepository()
account_repository = AccountRepository()
expense_repository = ExpenseRepository()


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = category_respository.get_queryset()


class TransactionsViewset(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = transaction_respository.get_queryset()


class AccountViewset(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = account_repository.get_queryset()


class ExpenseViewset(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = expense_repository.get_queryset()
