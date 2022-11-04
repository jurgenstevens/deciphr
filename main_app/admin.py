from django.contrib import admin
from .models import Song, Comment, Genre
# Register your models here.
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Genre)