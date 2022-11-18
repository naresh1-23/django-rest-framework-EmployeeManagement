from django.db import models
from .validations import validate_number
class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    contact = models.CharField(max_length = 10,validators=[validate_number])
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
    
