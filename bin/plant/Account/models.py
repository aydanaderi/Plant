from __future__ import unicode_literals
from django.db import models

class Information(models.Model) :
    username =  models.BigIntegerField()
    password = models.CharField(max_length = 100)
    newpassword = models.CharField(max_length = 100,default = '0')
    email = models.EmailField(max_length = 254)
    date = models.DateTimeField()
    profile = models.FileField()