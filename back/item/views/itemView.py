from django.shortcuts import render
from common.helpers.responseHelper import responseHelper
from item.models.item import item
from common.helpers.authTokenHelper import authTokenHelper
import json

def handleItems(request):

    dataset = []
    if("POST" == request.method):
        if(not authTokenHelper.validateToken(request) ):
            return responseHelper.getUnauthorizedResponse()

        payload = json.loads(request.body)
        new_item = item()
        new_item.setAll(payload)
        new_item.save()
        dataset = new_item.toDic()
    else:
        search_name = request.GET.get('name', False)
        if(False != search_name):
            related_records = item.find(item, {
                'conditions' : 'name LIKE %s AND deleted = 0',
                'bind' : ["%"+search_name+"%"]
            })
            dataset = item.getAllToArray(related_records)
        else :
            dataset = item.getAll(item)
        return responseHelper.getSuccessResponse(dataset)

def handleASpecifcItem(request, id):

    if(not authTokenHelper.validateToken(request) ):
        return responseHelper.getUnauthorizedResponse()

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

def handleCategoryItems(request, category_id):
    related_records = item.find(item, {
        'conditions' : 'category_id = %s',
        'bind' : [category_id]
    })
    return responseHelper.getSuccessResponse(item.getAllToArray(related_records))
