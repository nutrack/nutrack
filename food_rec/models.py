from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Food(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(max_length=100, default='', blank=True, null=True)
    calories = models.IntegerField(default=0, blank=True, null=True)
    protein = models.IntegerField(default=0, blank=True, null=True)
    fat = models.IntegerField(default=0, blank=True, null=True)
    carbs = models.IntegerField(default=0, blank=True, null=True)
    is_food = models.BooleanField(default=True);
    rating = models.IntegerField(default=0 , blank=True, null=True)
    rater = models.IntegerField(default=0 , blank=True, null=True)