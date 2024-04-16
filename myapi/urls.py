from django.urls import path, include

from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
]
