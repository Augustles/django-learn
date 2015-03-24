#coding=utf-8
from django.db import models

# Create your models here.
class Ask(models.Model):
    isvalid = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True, db_index=True)
    update_time = models.DateTimeField(auto_now=True)

    content = models.CharField(max_length=400)
    display_status = models.CharField(max_length=16, default='show')                    # admin check
    private = models.BooleanField(default=1)
    reply_status = models.CharField(max_length=16, default='unreply')    #unreply, replied, reject
    def __unicode__(self): # 显示具体object
        return self.content
class Answer(models.Model):
    isvalid = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    type = models.CharField(max_length=12, default='')
    content = models.CharField(max_length=1000)
    ask = models.ForeignKey(Ask)
    display_status = models.CharField(max_length=16, default='show')                    # admin check
    def __unicode__(self):
        return self.content
