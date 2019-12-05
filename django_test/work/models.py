from time import timezone

from django.db import models

# Create your models here.
from django import forms


class Users(models.Model):
    class Meta:
        db_table = 'work_users'
    username = models.CharField(max_length=20)
    headimg = models.FileField(upload_to='file') #定义上传的路径，相对于settings中的MEDIA_ROOT路径
    classfi = models.CharField(max_length=10)
    uptime = models.DateTimeField('上传日期')
    def __str__(self):
        return self.username

class UserInfo(models.Model):
    class Meta:
        db_table = 'work_userinfo'
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=11)
    image = models.FileField(upload_to='images')