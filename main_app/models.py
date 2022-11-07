from django.db import models
from django.urls import reverse

GENRES = (
    ('P', 'Pop'),
    ('R', 'Rock'),
    ('RB', 'R&B'),
    ('H', 'Hip Hop'),
    ('J', 'Jazz'),
    ('C', 'Country'),
    ('T', 'Techno'),
    ('D', 'Dubstep'),
    ('E', 'EDM'),
)

# Create your models here.
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


class Genre(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    genre_name = models.CharField(
        max_length=2,
        choices=GENRES,
        default="---",
        null=True
    )

    def __str__(self):
        return self.genre_name

    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"pk": self.pk})