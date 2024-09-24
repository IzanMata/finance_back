from django.db.models.query import QuerySet
from financial_management.models import Category

class CategoryRepository():

    def get_queryset(self) -> QuerySet[Category]:
        return Category.objects.all()