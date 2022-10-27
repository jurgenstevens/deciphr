from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.songs_index, name='songs'),
    path('songs/<int:song_id>/', views.songs_detail, name='detail'),
]