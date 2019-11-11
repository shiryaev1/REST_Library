from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=50)