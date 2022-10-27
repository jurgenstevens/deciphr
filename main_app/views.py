from curses.ascii import HT
from django.shortcuts import render
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