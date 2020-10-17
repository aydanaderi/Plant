from __future__ import unicode_literals
from django.db import models

class Information(models.Model) :
    username =  models.BigIntegerField()
    password = models.CharField(max_length = 100)
    newpassword = models.CharField(max_length = 100,default = '0')
    date = models.DateTimeField()
    time = models.CharField(max_length = 500)
    email = models.EmailField(max_length = 254)
    profile = models.FileField()
    random = models.IntegerField(max_length = 100000, default = 9999)