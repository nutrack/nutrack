from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=255)
    date = models.DateField()
    like = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    title = models.CharField(max_length=255)
    article_post = models.TextField()