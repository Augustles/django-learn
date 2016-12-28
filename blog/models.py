from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length = 180)
    def __unicode__(self):
        return self.title
    content = models.TextField()
    def __unicode__(self):
        return self.content
    pub_time = models.DateTimeField(auto_now_add=True)
