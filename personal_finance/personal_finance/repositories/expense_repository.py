from django.db.models.query import QuerySet
from financial_management.models import Expense

class ExpenseRepository():

    def get_queryset(self) -> QuerySet[Expense]:
        return Expense.objects.all()