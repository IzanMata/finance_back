from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Account(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = 'income', 'Income'
        EXPENSE = 'expense', 'Expense'
    
    class Periodicity(models.TextChoices):
        ONETYME = 'onetime', 'OneTime'
        MONTHLY = 'monthly', 'Monthly'
        ANNUAL = 'annual', 'Annual'

    type = models.CharField(max_length=7, choices=Type.choices)
    datetime = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    periodicity = models.CharField(max_length=7, choices=Periodicity.choices)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction_account')
    category = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction_category')

    def __str__(self) -> str:
        return f"{self.type.capitalize()}: {self.amount} ({self.description})"
    
class SavingsPlan(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='savings_plans_account')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.name