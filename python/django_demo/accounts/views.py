# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
def index(request):
    return render(request, 'index.html')


@csrf_protect
def signup(request):
    '''
    注册'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = UserCreationForm()
        return render_to_response("signup.html", {'form': form})


def profile(request):
    return render(request, 'profile.html')


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
            msg = "Invalid Password"
            return render_to_response('login.html', {'msg': msg})



def logout(request):
    pass
