from turtle import title
from django.db import models

# Create your models here.


class Api(models.Model):
    title=models.CharField(max_length=200)
    description =models.TextField(max_length=500)
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title