from django.db.models.query import QuerySet
from financial_management.models import Account


class AccountRepository:

    def get_queryset(self) -> QuerySet[Account]:
        return Account.objects.all()

    def update_balance(self, account: Account, new_balance: int) -> None:
        account.balance = new_balance
        account.save()
