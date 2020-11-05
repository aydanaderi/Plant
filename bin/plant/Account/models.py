from __future__ import unicode_literals
from django.db import models
from PIL import Image

class Information(models.Model) :
    id = models.AutoField(primary_key=True)
    username =  models.BigIntegerField()
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    date = models.DateTimeField()
    profile = models.ImageField(default = 'pic.jpg')
    def __str__(self):
        return str(self.username)

"""    def save(self, *args , **kwargs):
        super().save(*args , **kwargs)
        img = Image.open(self.profile.path)
        if img.height > 100 or img.weight > 100 :
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.profile.path)"""