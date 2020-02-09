from django.shortcuts import render
from common.baseResponder import baseResponder
from item.models.stock import stock
import json

def getStocksFroItem(render, item_id):
    br = baseResponder('application/json')
    stock_dataset = stock.getStocksForItem(item_id)
    return br.success(stock_dataset)


def handleSpecifcStock(request, id):

    related_stock = stock.getById(stock, id)
    br = baseResponder('application/json')
    if(False == related_stock):
        return br.success({})
    if("POST" == request.method):
        payload = json.loads(request.body)
        related_stock.setAll(payload)
        if(False == related_stock.save()):
            return br.conflict('something went wrong')
           
    return br.success(related_stock.toDic())