# from curses.ascii import HT
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Song
from .forms import CommentForm, GenreForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Define the home view
def home(request):
    return render(request,'home.html')

#  create an all_songs function here to attain all songs in the landing page!
def about(request):
    return render(request, 'about.html')

def all_songs(request):
    songs = Song.objects.all()
    return render(request, 'songs/all_songs.html', {
        'all_songs' : songs
})

def songs_index(request):
    songs = Song.objects.filter(user=request.user)
    return render(request, 'songs/index.html', {
        'songs' : songs
})

def songs_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    comment_form = CommentForm()
    genre_form = GenreForm()
    return render(request, 'songs/detail.html', {
        'song': song,
        'comment_form': comment_form,
        'genre_form': genre_form
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
        new_comment.user_id = request.user.id
        new_comment.song_id = song_id
        new_comment.save()
    return redirect('detail', song_id=song_id)


class SongCreate(CreateView):
    model = Song
    fields = ['song_name','artist_name', 'album_name', 'song_link', 'attempted_lyrics']
    success_url = '/songs/'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the song
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class SongUpdate(UpdateView):
    model = Song
    fields = ['song_name','artist_name', 'album_name', 'song_link', 'attempted_lyrics']

class SongDelete(DeleteView):
    model = Song
    success_url = '/songs/'

def add_genre(request, song_id):
    #create the ModelForm using the data in request.POST
    form = GenreForm(request.POST)
    #validate the form
    if form.is_valid():
        #don't save the form to the db until it has song_id assigned
        new_genre = form.save(commit=False)
        new_genre.song_id = song_id
        new_genre.save()
    return redirect('detail', song_id=song_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)