from django.shortcuts import render
from django.http import HttpResponse
from common.baseResponder import baseResponder
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
