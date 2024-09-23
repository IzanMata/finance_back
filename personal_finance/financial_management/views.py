from rest_framework import viewsets
from financial_management.models import Category
from personal_finance.repositories.category_repository import CategoryRepository
from personal_finance.serializers.category_serializer import CategorySerializer

category_respository = CategoryRepository()

class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = category_respository.get_all()