from django.db.models.query import QuerySet
from financial_management.models import Category
from django.core.exceptions import ObjectDoesNotExist

class CategoryRepository():

    def get_all(self) -> QuerySet[Category]:
        return Category.objects.all()