# Generated by Django 5.1.1 on 2024-09-24 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transaction_category",
                to="financial_management.category",
            ),
        ),
    ]
