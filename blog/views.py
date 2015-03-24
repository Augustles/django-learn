#coding=utf-8
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blogpost
from django.template import loader,Context
def index(request):
    c = Blogpost.objects.all()
    t = loader.get_template('index.html')
    context = Context({'c':c})
    return HttpResponse(t.render(context))
def detail(request,blog_id):
    c = Blogpost.objects.all()
    t = loader.get_template('archive.html')
    context = Context({'c':c})
    return HttpResponse(t.render(context))

def comment(request,blog_id):
    return HttpResponse('comment %s' %blog_id)
def thanks(request,blog_id):
    return HttpResponse('thanks %s' %blog_id)



'''
from blog.models import Blogpost # 导入Blogpost模型
from django.http import HttpResponse #导入HttpResponse
from django.shortcuts import render # 导入render
from django.template import loader,Context # 导入template下的loader，和Context

def archive(request):
    posts = Blogpost.objects.all() # 获取Blogpost所有对象
    t = loader.get_template('archive.html') # 加载archive模板
    c = Context()


'''
