from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def index(request):
    return HttpResponse('Hello, World!')


def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>Tt is now %s</body></html>" % now
    return HttpResponse(html)
