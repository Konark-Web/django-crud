from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created_date',)

    def save(self, *args, **kwargs):
        self.modified_date = timezone.now()
        super(Post, self).save(*args, **kwargs)
