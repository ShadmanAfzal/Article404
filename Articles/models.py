import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    Phone_Number = models.IntegerField(default=0)
    Address = models.CharField(max_length=100, default="")
    profile_pic = models.ImageField(upload_to='Media', blank=True, default='Media/avatar.png')


class Post(models.Model):
    category = models.CharField(max_length=100, default="Gaming")
    Author = models.CharField(max_length=100, default="anonymous")
    DOP = models.DateTimeField(datetime.datetime.now)
    Content = models.TextField()
    Title = models.CharField(default="No Title", max_length=100)
    Slug = models.CharField(blank=False, max_length=100)
    tag = models.CharField(blank=True, default="None", max_length=50)
    Post_Image = models.ImageField(upload_to='Media/Post', blank=False, default=None)
    Post_Image1 = models.ImageField(upload_to='Media/Post', blank=True, default=None)
    Post_Image2 = models.ImageField(upload_to='Media/Post', blank=True, default=None)

    def __str__(self):
        return self.Title


class Comments(models.Model):
    Author = models.CharField(max_length=100, default="anonymous")
    Date = models.DateTimeField(default=datetime.datetime.now)
    Content = models.TextField()
    Slug = models.CharField(blank=False, max_length=100, default="None")
    author_pic = models.ImageField(upload_to='Media', default='Media/avatar.png', blank=True)

    def __str__(self):
        return self.Content


class contact(models.Model):
    choice = models.CharField(max_length=100, default="Experience")
    username = models.CharField(max_length=100, default=None, blank=False)
    email = models.EmailField(default=None, blank=False)
    feedback = models.TextField(default=None, blank=False)

    def __str__(self):
        return f"Send by {self.username} from {self.email}"
