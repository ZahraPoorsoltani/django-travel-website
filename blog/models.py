from django.db import models
import datetime
from time import timezone
from django.contrib.auth.models import User
# from accounts.models import CustomUser 
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(User,models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    login_require = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:blog_single',kwargs={'post_id':self.id})
