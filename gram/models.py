
from distutils.command.upload import upload
from importlib.machinery import OPTIMIZED_BYTECODE_SUFFIXES
from random import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=254, unique=True)
    age = models.IntegerField(null=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email


class Albums(models.Model):
    image = models.FileField(upload_to = 'media/')
    publish = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    caption = models.CharField(blank=True,max_length=100,null=True)
    position_coordinates_top = models.FloatField(blank=True,null=True)
    position_coordinates_down = models.FloatField(blank=True,null=True)
    position_coordinates_left = models.FloatField(blank=True,null=True)
    position_coordinates_right = models.FloatField(blank=True,null=True)
    font_color= models.CharField(blank=True,max_length=50,null=True)

    def __str__(self):
        return str(self.id)

class Drafts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    album = models.ForeignKey(Albums,on_delete=models.PROTECT)

    def __str_(self):
        return str(self.album.id)

class Hashtags(models.Model):
    hashtag = models.CharField(blank=True,max_length=1000,null=True)
    album = models.ForeignKey(Albums,on_delete=models.PROTECT)

    def __str_(self):
        return str(self.hashtag)