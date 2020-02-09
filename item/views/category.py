from django.shortcuts import render
from common.baseResponder import baseResponder
from item.models.category import category
import json


def handleCategories(request):
    dataset = {}
    br = baseResponder('application/json')
    if("POST" == request.method):
        payload = json.loads(request.body)
        new_category = category()
        new_category.setAll(payload)
        new_category.save()
        dataset = new_category.toDic()
    else:
        dataset = category.getAll(category)
    return br.success(dataset)

def handleSpecificCategory(request, id):
    related_category = category.getById(category, id)
    br = baseResponder('application/json')
    if(False == related_category):
        return br.success({})
    if("POST" == request.method):
        payload = json.loads(request.body)
        related_category.setAll(payload)
        if(False == related_category.save()):
            return br.conflict('something went wrong')
           
    return br.success(related_category.toDic())