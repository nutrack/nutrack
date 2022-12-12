from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator 

# Create your models here.
class Nutrack(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    goal=models.IntegerField(default=0,validators=[MinValueValidator(1)])

