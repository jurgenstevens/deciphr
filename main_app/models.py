from django.db import models

# Create your models here.
class Song(models.Model):
    original_poster = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    song_link = models.CharField(max_length=100)
    attempted_lyrics = models.TextField(max_length=250)
    upvotes = models.IntegerField
