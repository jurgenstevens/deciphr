# from curses.ascii import HT
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Song
from .forms import CommentForm

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
    comment_form = CommentForm()
    return render(request, 'songs/detail.html', {
        'song': song,
        'comment_form': comment_form,
    })

# Comment Functionality

def add_comment(request, song_id):
    # create the ModelForm using the data in request.POST
    form = CommentForm(request.POST)
    # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the song_id assigned
        new_comment = form.save(commit=False)
        new_comment.song_id = song_id
        new_comment.save()
    return redirect('detail', song_id=song_id)


class SongCreate(CreateView):
    model = Song
    fields = ['song_name','artist_name', 'album_name', 'song_link', 'attempted_lyrics']
    success_url = '/songs/'

class SongUpdate(UpdateView):
    model = Song
    fields = ['song_name','artist_name', 'album_name', 'song_link', 'attempted_lyrics']

class SongDelete(DeleteView):
    model = Song
    success_url = '/songs/'

