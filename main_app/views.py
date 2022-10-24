from curses.ascii import HT
from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

class Song:
    def __init__(self, original_poster, song_name, artist_name, album_name, song_link, attempted_lyrics):
        self.original_poster = original_poster
        self.song_name = song_name
        self.artist_name = artist_name
        self.album_name = album_name
        self.song_link = song_link
        self.attempted_lyrics = attempted_lyrics

songs = [
    Song('jurgensteves', 'Dejame En Paz', 'Holy Wave', 'Evil Hits', 'https://www.youtube.com/watch?v=-ZGrgna1s3s&ab_channel=HolyWave-Topic', 'N/A')
]

# Define the home view
def home(request):
    return HttpResponse('<h1>Welcome To Deciphr.</h1>')

#  create an all_songs function here to attain all songs in the landing page!

def about(request):
    return render(request, 'about.html')

def songs_index(request):
    return render(request, 'songs/index.html', {
        songs
    })