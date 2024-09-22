from django.db import models
from django.utils import timezone

class User(models.Model):
    pass

class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = 'income', 'Income'
        EXPENSE = 'expense', 'Expense'
    
    class Periodicity(models.TextChoices):
        ONETYME = 'onetime', 'OneTime'
        MONTHLY = 'monthly', 'Monthly'
        ANNUAL = 'annual', 'Annual'

    type = models.CharField(max_length=7, choices=Type.choices)
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    periodicity = models.CharField(max_length=7, choices=Periodicity.choices)

    def __str__(self) -> str:
        return f"{self.type.capitalize()}: {self.amount} ({self.description})"