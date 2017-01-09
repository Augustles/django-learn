#coding=utf-8
# Create your views here.
# 1.7 new JsonResponse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from blog.models import Blogpost, Post
from django.template import loader,Context
def index(request):
    c = Post.objects.filter()
    # out = []
    # for x in c:
        # tmp = (x.title, x.content, x.pub_time)
        # out.append(tmp)
    return JsonResponse({'result': c.to_json()})
def detail(request,blog_id):
    c = Blogpost.objects.all()
    context = Context({'c':c})
    return HttpResponse(context)

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
