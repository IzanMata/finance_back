from rest_framework import serializers
from financial_management.models import Account

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = '__all__'