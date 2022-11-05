from django.forms import ModelForm
from .models import Comment, Genre

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['song_comment']

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name']