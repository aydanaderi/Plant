from django.db import models

class Plant(models.Model) :
    amount = (
        ('l' , 'low'),
        ('m' , 'middle'),
        ('h' , 'high'),
    )
    answer = (
        ('y' , 'yes'),
        ('n' , 'no'),
    )
    name = models.CharField(max_length = 500)
    English_name = models.CharField(max_length = 500)
    irrigation_quantity = models.CharField(max_length = 1,choices = amount)
    irrigation = models.CharField(max_length = 500)
    temprature_quantity = models.CharField(max_length = 500)
    temprature = models.TextField()
    light_quantity = models.CharField(max_length = 1,choices = amount)
    light = models.TextField()
    humidity_quantity = models.CharField(max_length = 1,choices = amount)
    humidity = models.TextField()
    soil = models.TextField()
    fertilizer = models.TextField()
    problems = models.TextField()
    potting = models.TextField()
    poisonous = models.CharField(max_length = 1,choices = answer)
    sensibility = models.CharField(max_length = 1,choices = amount)



