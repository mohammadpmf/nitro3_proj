from django.urls import path, include

from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('series/', views.serial_list),
    path('series/<int:pk>/', views.serial_detail),
    path('music/', views.music_list),
    path('music/<int:pk>/', views.music_detail),
]
