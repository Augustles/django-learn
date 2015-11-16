# coding=utf8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django import forms
from online.models import User
# 定义表单模型


class UserForm(forms.Form):
    username = forms.CharField(label='用户名：')
    password = forms.CharField(label='密码：', widget=forms.PasswordInput())


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userall = User.objects.all()
            if username not in userall:
                User.objects.create(username=username, password=password)
                return render_to_response('online/login.html', {'username': username})
            else:
                return HttpResponse('you are register')
    else:
        uf = UserForm()
    return render_to_response('online/register.html', {'uf': uf})


def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(
                username__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/online/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                # 比较失败，停留login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('online/login.html', {'uf': uf})

# 登陆成功


def index(request):
    username = request.COOKIES.get('username', '')
    if username:
        return render_to_response('online/index.html', {'username': username})
    else:
        return redirect('/online/login')

# 退出


def logout(request):
    response = HttpResponse('logout !!')
    response.delete_cookie('username')
    return response
