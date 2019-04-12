from django.db import models


class Artist(models.Model):
    name = models.CharField()


class Album(models.Model):
    name = models.CharField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    name = models.CharField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
