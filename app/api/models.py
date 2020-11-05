from django.db import models


class Artist(models.Model):

    name = models.CharField(max_length=150)
    href = models.URLField()
    spotify_id = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    uri = models.CharField(max_length=255)
    external_urls = models.JSONField()

    def __str__(self):
        return self.name
