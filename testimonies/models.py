from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Testimony(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    testimony = models.TextField()