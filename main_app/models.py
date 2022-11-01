from django.db import models
from django.urls import reverse

# Create your models here.
# class Playlist(models.Model):
#     playlist_name = models.CharField(max_length=50)
#     playlist_description = models.CharField(max_length=50)

#     def __str__(self):
#         return self.playlist_name

#     def get_absolute_url(self):
#         return reverse("playlist_detail", kwargs={"pk": self.pk})


class Song(models.Model):
    original_poster = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    song_link = models.CharField(max_length=100)
    attempted_lyrics = models.TextField(max_length=255)
    upvotes = models.IntegerField(null=True)
    # add user later

    def __str__(self):
        return self.song_name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"song_id": self.id})
    
    
class Comment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_comment = models.TextField(max_length=255, null=True)
    comment_upvotes = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment created at {self.created}"

