# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms

def index(request):
    '''用户的个人页面
    '''
    return render(request, 'auth/index.html')

def register(request):
    '''
    注册'''

def login(request):
     if requset.method == 'GET':
        form = LoginForm()
        return render(request, 'login')

   pass


def logout(request):
    pass


# 登录表单
class LoginForm(forms.Form):
    '''Login From'''
    error = forms.CharField()
    username = forms.CharField(label=u"昵称", max_length=30, widget=forms.TextInput(attrs={'size': 20,}))
    password = forms.PasswordInput(label=u'密码', max_length=30, widget=forms.PasswordInput(attrs={'size': 20,}))
