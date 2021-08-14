from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class CategoryList(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    img=models.ImageField(upload_to='categorypics',blank=True)
    slug=models.SlugField(unique=True)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name
    
    
    
    
    @property
    def image_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

class Item(models.Model):
    sno=models.AutoField(primary_key=True)
    category=models.ForeignKey(CategoryList,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    title=models.CharField(max_length=200)
    # videourl=models.URLField(max_length=200)
    video = EmbedVideoField()  # same like models.URLField()
    modnamever=models.CharField(max_length=100,default="will be updated shortly")
    modername=models.CharField(max_length=150)
    moderyt=models.URLField(blank=True)
    moderpatreon=models.URLField(blank=True)
    modlink=models.URLField()
    fileurl=models.URLField(blank=True)
    desc=models.TextField()
    publish=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-title',)

    def __str__(self):
        return self.title

    
class VideoComment(models.Model):
    srno = models.AutoField(primary_key=True)
    comment=models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article = models.ForeignKey(Item,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + "..." + "by " + self.user.username

