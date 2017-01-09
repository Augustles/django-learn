from django.db import models
from datetime import datetime as dte

from mongoengine import connect, Document, \
    DateTimeField, ListField, IntField, BooleanField, \
    DictField, StringField

connect('web')

class Post(Document):
    title = StringField(required=True)
    url = StringField(required=True)
    create_time = DateTimeField(default=dte.now())
    update_time = DateTimeField(default=dte.now())
    tag = StringField()
    commit = ListField(field=ListField(field=StringField()))
    is_show = IntField(default=0)
    is_closed = BooleanField(default=False)
    extra_info = DictField()
    def __unicode__(self):
        return self.title

    meta = {
        'indexes': [
            'title',
            'url',
        ],
        'collection': 'jianshu',
    }



# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length = 180)
    def __unicode__(self):
        return self.title
    content = models.TextField()
    def __unicode__(self):
        return self.content
    pub_time = models.DateTimeField(auto_now_add=True)
