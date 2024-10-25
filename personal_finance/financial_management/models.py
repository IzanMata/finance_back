from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Account(models.Model):

    user: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    amount: int = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.user.email}"


class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # image = models.TextField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name.capitalize()}"


class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"

    type = models.CharField(max_length=7, choices=Type.choices)
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    description = models.CharField(max_length=255)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transaction_account"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="transaction_category"
    )

    def __str__(self) -> str:
        return f"{self.type.capitalize()}: {self.amount} ({self.description})"


class Expense(models.Model):
    class ExpenseType(models.TextChoices):
        DAILY = "daily", "Daily"
        WEEKLY = "weekly", "Weekly"
        MONTHLY = "monthly", "Monthly"
        ANNUALLY = "annually", "Annually"

    description = models.CharField(max_length=255)
    expense_type = models.CharField(
        max_length=10,
        choices=ExpenseType.choices,
        default=ExpenseType.MONTHLY,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="expense_category"
    )

    def __str__(self) -> str:
        return f"{self.description} - {self.expense_type} - {self.amount}"


class SavingsPlan(models.Model):

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="savings_plans_account"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
