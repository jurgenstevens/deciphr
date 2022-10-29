# from curses.ascii import HT
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Song

# Define the home view
def home(request):
    return render(request,'home.html')

#  create an all_songs function here to attain all songs in the landing page!
def about(request):
    return render(request, 'about.html')

def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', {
        'songs' : songs
})

def songs_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'songs/detail.html', {
        'song': song
    })

class SongCreate(CreateView):
    model = Song
    fields = ['song_name','artist_name', 'album_name', 'song_link', 'attempted_lyrics']