from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class caloryInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    calory=models.IntegerField(default=0)
