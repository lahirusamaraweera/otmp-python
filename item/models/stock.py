
from django.db import models
from common.baseModel import BaseModel
from item.models.item import item

class stock(models.Model, BaseModel):
    name = models.CharField(max_length=200)
    manufacture_date = models.DateField()
    expire_date = models.DateField()
    stock_code = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    deleted = models.BooleanField(default=False)
    qty = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    is_active = models.BooleanField(default=False)
    item = models.ForeignKey(
        'item',
        on_delete=models.PROTECT,
    )

    def toDic(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "price" : float(self.price),
            "qty" : float(self.qty),
            "stock_code" : self.stock_code,
            "is_active" : self.is_active,
            "deleted" : self.deleted,
            "item" : self.item.toDic()
        }
        
    @staticmethod
    def getStocksForItem(item_id):
        try:
            stocks = stock.objects.filter(item_id=item_id)
        except stock.DoesNotExist:
            return False
        return stock.getAllToArray(stocks)