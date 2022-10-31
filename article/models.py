from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=255)
    date = models.DateField()
    like = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    title = models.CharField(max_length=255)
    article_post = models.TextField()

class Comment(models.Model):
    art = models.ForeignKey(Article,on_delete=models.CASCADE, null=True, blank=True)
    user = user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    comment_post = models.TextField()
    artid = models.DecimalField(max_digits=5, decimal_places=0, default=0)