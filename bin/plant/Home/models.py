from django.db import models

class Plant(models.Model) :
    name = models.CharField()
    English_name = models.CharField()
    irrigation_quantity = models.CharField()
    irrigation = models.CharField()
    temprature_quantity = models.CharField()
    temprature = models.TextField()
    light_quantity = models.CharField()
    light = models.TextField()
    humidity_quantity = models.CharField()
    humidity = models.TextField()
    soil = models.TextField()
    fertilizer = models.TextField()
    problems = models.TextField()
    potting = models.TextField()
    poisonous = models.CharField()
    sensibility = models.CharField()



