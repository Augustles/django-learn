#coding=utf-8
from django.db import models

# Create your models here.
class User(models.Model): # 创建User表
    username = models.CharField(max_length = 50) # username fields
    password = models.CharField(max_length = 50) # Create password fields
    email = models.EmailField(blank=True) # Create email fields
    headImg = models.FileField(blank=True,upload_to='./upload') # 创建headImg文件上传路径字段
    def __unicode__(self):
        return self.username # 修正显示object问题
