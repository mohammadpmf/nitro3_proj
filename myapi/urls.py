from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views
from . import views_extra_part

schema_view = get_schema_view(
    openapi.Info(
        title="Movies API",
        default_version="v1",
    ),
    public=True, # defalut e public=False hast. age kar nakard in khat ro vardaram
)

router = DefaultRouter()
router.register('movies', views.MovieViewSet, basename='movie')
router.register('series', views.SerialViewSet, basename='serial')
router.register('music', views.MusicViewSet, basename='music')
router.register('staff', views.StaffViewSet, basename='staff')


urlpatterns = [
    path('', include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('get_sms/', views_extra_part.get_sms, name='get_sms')
]

# urlpatterns = [
#     path('movies/', views.MovieList.as_view(), name='movies'),
#     path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
#     path('series/', views.SerialList.as_view(), name='series'),
#     path('series/<int:pk>/', views.SerialDetail.as_view(), name='serial-detail'),
#     path('music/', views.MusicList.as_view(), name='musics'),
#     path('music/<int:pk>/', views.MusicDetail.as_view(), name='music-detail'),
# ]
