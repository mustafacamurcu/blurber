from django.db import models
from utils import pkgen

# Create your models here.

class Genre(models.Model):
    id = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    title_options = models.TextField()
    author_options = models.TextField()
    descr_options = models.TextField()

    def __unicode__(self):
        return self.name


class Blurb(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=pkgen)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    descr = models.TextField()
    genre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

