from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # new route used to show a form and create, read/view update and delete songs
    path('songs/', views.songs_index, name='index'),
    path('songs/<int:song_id>/', views.songs_detail, name='detail'),
    path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
    path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
    # new route used to show a form and create,read/view update and delete comments
    path('songs/<int:song_id>/add_comment/', views.add_comment, name='add_comment'),
    # new route used to show a form and create,read/view update and delete genre
    path('songs/<int:song_id>/add_genre/', views.add_genre, name='add_genre'),
]