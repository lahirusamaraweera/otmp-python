from django.db import models
from common.baseModel import BaseModel

class item(models.Model, BaseModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length = 500)
    item_code = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.CharField(max_length=10)
    deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(
        'category',
        on_delete=models.PROTECT,
    )

    def toDic(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "price" : float(self.price),
            "currency" : self.currency,
            "description" : self.description,
            "is_active" : self.is_active,
            "deleted" : self.deleted,
            "category" : self.category.toDic()
        }

class category(models.Model, BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def toDic(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description
        } 