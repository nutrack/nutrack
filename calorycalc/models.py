from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here

class caloryInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    calory=models.IntegerField(default=0)
