from django.db import models
from django.utils import timezone

# 博客文章model
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str_(self):
        return self.title