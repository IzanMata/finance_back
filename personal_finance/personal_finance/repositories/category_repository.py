from django.db.models.query import QuerySet
from financial_management.models import Category

class CategoryRepository():

    def get_all(self) -> QuerySet[Category]:
        return Category.objects.all()
        
    def get_by_id(self, id : int):
        pass