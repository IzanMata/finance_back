from rest_framework import serializers
from financial_management.models import Transaction
from personal_finance.serializers.category_serializer import CategorySerializer


class TransactionSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"
