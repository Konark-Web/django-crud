from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
