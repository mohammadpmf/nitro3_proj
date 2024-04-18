from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('movies', views.MovieViewSet, basename='movie')
router.register('series', views.SerialViewSet, basename='serial')
router.register('music', views.MusicViewSet, basename='music')


urlpatterns = [
    path('', include(router.urls)),
]


# urlpatterns = [
#     path('movies/', views.MovieList.as_view(), name='movies'),
#     path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
#     path('series/', views.SerialList.as_view(), name='series'),
#     path('series/<int:pk>/', views.SerialDetail.as_view(), name='serial-detail'),
#     path('music/', views.MusicList.as_view(), name='musics'),
#     path('music/<int:pk>/', views.MusicDetail.as_view(), name='music-detail'),
# ]
