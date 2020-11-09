from django.db import models
from django.contrib.postgres.fields import JSONField


class Artist(models.Model):

    name = models.CharField(max_length=150)
    href = models.URLField()
    spotify_id = models.CharField(max_length=150, unique=True)
    type = models.CharField(max_length=100)
    uri = models.CharField(max_length=255)
    external_urls = JSONField()

    def __str__(self):
        return self.name
