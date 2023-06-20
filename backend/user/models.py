from django.db import models

# Create your models here.

class UserModel(models.Model):
    username=models.CharField(max_length=50, verbose_name='유저아이디')
    password=models.CharField(max_length=50, verbose_name='비밀번호')
