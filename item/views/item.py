from django.shortcuts import render
from common.helpers.responseHelper import responseHelper
from item.models.item import item
import json

def handleItems(request):
    if(not responseHelper.isTokenInvalid(request)):
        return responseHelper.getUnauthorizedResponse()
    
    dataset = {}
    br = responseHelper('application/json')
    if("POST" == request.method):
        payload = json.loads(request.body)
        new_item = item()
        new_item.setAll(payload)
        new_item.save()
        dataset = new_item.toDic()
    else:
        dataset = item.getAll(item)
    return br.success(dataset)

def handleASpecifcItem(request, id):

    related_item = item.getById(item, id)
    br = responseHelper('application/json')
    if(False == related_item):
        return br.success({})
    if("POST" == request.method):
        payload = json.loads(request.body)
        related_item.setAll(payload)
        if(False == related_item.save()):
            return br.conflict('something went wrong')
           
    return br.success(related_item.toDic())
