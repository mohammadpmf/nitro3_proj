from django.urls import path, include

from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movies'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('series/', views.SerialList.as_view(), name='series'),
    path('series/<int:pk>/', views.SerialDetail.as_view(), name='serial-detail'),
    path('music/', views.MusicList.as_view(), name='musics'),
    path('music/<int:pk>/', views.MusicDetail.as_view(), name='music-detail'),
]
