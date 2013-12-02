from django.shortcuts import render
from django.http import HttpResponse
from django.http import

def index(request):
    welcome_msg = {"w": _(u"欢迎您，游客")}
    if request.user.is_authenticated():
        welcome_msg['w'] = _(u"欢迎您 %s!") % request.user.username
    return render(request, 'auth/index.html', welcome_msg)


def register(request):
    pass


def login(request):
    pass


def logout(request):
    pass
