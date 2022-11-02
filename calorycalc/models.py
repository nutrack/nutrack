from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here


class caloryInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    calory=models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(100)])
