from django.shortcuts import render
from common.baseResponder import baseResponder
from item.models.item import item
import json

def handleItems(request):
    dataset = {}
    br = baseResponder('application/json')
    if("POST" == request.method):
        payload = json.loads(request.body)
        new_item = item()
        new_item.setAll(payload)
        new_item.save()
        dataset = new_item.toDic()
    else:
        dataset = item.getAll(item)
    return br.success(dataset)

def handleSpecifcItem(request, id):

    related_item = item.getById(item, id)
    br = baseResponder('application/json')
    if(False == related_item):
        return br.success({})
    if("POST" == request.method):
        payload = json.loads(request.body)
        related_item.setAll(payload)
        if(False == related_item.save()):
            return br.conflict('something went wrong')
           
    return br.success(related_item.toDic())
