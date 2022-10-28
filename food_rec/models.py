from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    is_food = models.BooleanField(default=True)
    rating = models.IntegerField(default=0);
    def __str__(self):
        return self.name