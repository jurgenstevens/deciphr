from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.songs_index, name='songs'),
    path('songs/<int:song_id>/', views.songs_detail, name='detail'),
    # new route used to show a form and create a cat
    path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
]