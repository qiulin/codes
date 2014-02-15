# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth


def index(request):
    return render(request, 'index.html')
def register(request):
    '''
    注册'''
    import pdb; pdb.set_trace()  # XXX BREAKPOINT


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/accounts/profile")
        else:
            msg = "Invalid Password!"
            return render(request, 'login.html', msg=msg)



def logout(request):
    pass
