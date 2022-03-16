from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255,unique = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 255)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    image = models.ImageField(upload_to='blogspot/images',blank = True, null = True)
    body = RichTextField(blank = True, null = True)
    date = models.DateField(auto_now_add = True)

class Comment(models.Model):
    desc = models.CharField(max_length = 1000)
    author = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    
