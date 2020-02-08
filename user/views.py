from django.shortcuts import render
from django.http import HttpResponse
from common.base import baseResponder
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def test(request):
    dic = {'abc' : 'tesst'}
    br = baseResponder('application/json')
    br.setHeaders(dic)
    sample_da = {
        'name' : 2
    }
    return br.success(sample_da)
