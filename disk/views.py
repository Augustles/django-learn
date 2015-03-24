#coding=utf-8

from django import forms
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from disk.models import User

# forms models
class UserForm(forms.Form):
    username = forms.CharField(label='请输入你的名字：')
    headImg = forms.FileField(label='上传头像：')

# views
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            user = User()
            user.username= username
            user.headImg = headImg
            user.save()
            return HttpResponse('yes')
    else:
        uf = UserForm()
    return render_to_response('disk/register.html',{'uf':uf})
