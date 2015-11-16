# Create your views here.
#coding=utf-8

from django.http import HttpResponse,Http404 # import HttpResponse
from ask.models import Ask,Answer # import Ask,Answer models
from django.template import loader,Context # import loader,Context models
from django.shortcuts import render,get_object_or_404 # import render
from django import forms
from django.shortcuts import render_to_response

# 创建表单模型
class AskForm(forms.Form):
    code = forms.CharField(label='请添加你的问题：',max_length=200)

class AnswerForm(forms.Form):
    answer = forms.CharField(label='请添加你的回答：',max_length=200)

# views
def index(request): # 定义一个index视图
    ask_list = Ask.objects.all() # 获取Ask模型所有元素
    temp = loader.get_template('ask/index.html') # 加载index.html模板
    context = Context({'ask_list':ask_list}) # 用Content函数来xianlan
    return HttpResponse(temp.render(context)) # 模板用render解析
def answer(request):
    answer_list = Answer.objects.all()
    context = Context({'answer_list':answer_list})
    return render(request,'ask/answer.html',context)

def answer_add(request):
    ask_id = str(request.META.get('HTTP_REFERER',"/").split('/')[-2])
    answer = Answer()
    # return HttpResponse(ask_id)
    answer.ask_id = ask_id
    if request.method == 'POST':
        af = AnswerForm(request.POST)
        if af.is_valid():
            # 获取表单内容
            content = af.cleaned_data['answer']
            answer.content = content
            answer.save()
            return render_to_response('ask/answer_add_done.html',{'content':content})
    else:
        af = AnswerForm()
    return render_to_response('ask/answer_add.html',{'af':af})


def detail(request,ask_id):
    # try:
    #     ask = Ask.objects.get(pk=ask_id)
    # except Ask.DoesNotExist:
    #     raise Http404
    ask = get_object_or_404(Ask,pk=ask_id)
    ask_reply = ask.answer_set.all()
    # return HttpResponse(ask_reply.get().content)
    context = Context({'ask_reply':ask_reply})
    return render(request,'ask/detail.html',context)
def ask_add(request):
    if request.method == 'POST':
        af = AskForm(request.POST)
        if af.is_valid():
            # 获取表单内容
            content = af.cleaned_data['code']
            ask = Ask()
            ask.content = content
            ask.save()
            return render_to_response('ask/add_done.html',{'content':content})
    else:
        af = AskForm()
    return render_to_response('ask/add.html',{'af':af})


    # return render(request,'ask/add.html')
def add_done(request):
    return render(request,'ask/add_done.html')

