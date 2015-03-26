#coding=utf-8
from django.shortcuts import render # import render
from django import forms # import forms not form
from django.shortcuts import render_to_response # import 比较与render区别
from django.http import HttpResponse,HttpResponseRedirect # import
from account.models import User

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：')
    headImg = forms.FileField(label='请上传图片',max_length='200')

# Create your views here.
def index(request):
    account_list = User.objects.all()
    context = {'account_list':account_list}
    return render(request,'account/index.html',context)
def login(request):
    return HttpResponse('account login page')
def register(request):
    if request.method == "POST": # 判定request是否为post
        uf = UserForm(request.POST,request.FILES) # 是就把post数据和file路径都给变量uf
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            headImg = uf.cleaned_data['headImg']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            user.headImg = headImg
            user.email = email
            user.save()
            #返回注册成功页面
            return render_to_response('account/success.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('account/register.html',{'uf':uf})
