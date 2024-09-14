from django.db import models

# Create your models here.
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    url = models.URLField(max_length=10000)
    content = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=10000)

    def __str__(self):
        return self.title
