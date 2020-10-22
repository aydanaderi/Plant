from django.db import models

class Plant(models.Model) :
    amount = (
        ('low' , 'low'),
        ('middle' , 'middle'),
        ('high' , 'high'),
    )
    quantity = (
        ('low', 'low'),
        ('middle', 'middle'),
        ('high', 'high'),
    )
    answer = (
        ('yes' , 'yes'),
        ('no' , 'no'),
    )
    name = models.CharField(max_length = 500 , default = '')
    English_name = models.CharField(max_length = 500,default = '')
    irrigation_quantity = models.CharField(max_length = 10,choices = amount,default = '')
    irrigation = models.CharField(max_length = 10000,default = '')
    temprature_quantity = models.CharField(max_length = 500,default = '')
    temprature = models.CharField(max_length = 10000,default = '')
    light_quantity = models.CharField(max_length = 10,choices = amount,default = '')
    light = models.CharField(max_length = 10000,default = '')
    humidity_quantity = models.CharField(max_length = 10,choices = amount,default = '')
    humidity = models.CharField(max_length = 10000,default = '')
    soil = models.CharField(max_length = 10000,default = '')
    fertilizer = models.CharField(max_length = 10000,default = '')
    problems = models.CharField(max_length = 10000,default = '')
    potting = models.CharField(max_length = 10000,default = '')
    poisonous = models.CharField(max_length = 5,choices = answer,default = '')
    sensibility = models.CharField(max_length = 10,choices = amount,default = '')



