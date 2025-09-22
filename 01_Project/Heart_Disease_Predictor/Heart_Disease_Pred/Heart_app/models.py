from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']

class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    mission_statement = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Page Content"
