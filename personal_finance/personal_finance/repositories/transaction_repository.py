from django.db import transaction as db_transaction
from django.db.models.query import QuerySet

from financial_management.models import Account, Transaction


class TransactionRepository:

    def get_queryset(self) -> QuerySet[Transaction]:
        return Transaction.objects.all()

    @db_transaction.atomic
    def perform_transaction(self, account: Account, transaction: Transaction) -> None:

        transaction_type = transaction.type
        transaction_amount = transaction.amount

        if transaction_type == "DEPOSIT":
            account.balance += transaction_amount
        elif transaction_type == "WITHDRAWAL":
            if account.balance < transaction_amount:
                raise ValueError("Insufficient funds")
            account.balance -= transaction_amount

        self.update_balance(account, account.balance)
        Transaction.objects.create(account, transaction_type, transaction_amount)
