from django.shortcuts import render
from common.baseResponder import baseResponder
from .models import item

# Create your views here.

def getAllItems1(request):
    dataset = []
    items = item.objects.all()
    for item_object in items:
        dataset.append(item_object.toDic())
    br = baseResponder('application/json')
    return br.success(dataset)

def getAllItems(request):
    br = baseResponder('application/json')
    dataset = item.getAll(item)
    return br.success(dataset)
