from django.urls import path, include

from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movies'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('series/', views.serial_list, name='series'),
    path('series/<int:pk>/', views.serial_detail, name='serial-detail'),
    path('music/', views.music_list, name='musics'),
    path('music/<int:pk>/', views.music_detail, name='music-detail'),
]
