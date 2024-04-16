from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieSerializer

from .models import Movie

@api_view()
def movie_list(request):
    movies_queryset = Movie.objects.all().select_related('director')
    serializer = MovieSerializer(movies_queryset, many=True)
    return Response(serializer.data)

@api_view()
def movie_detail(request, pk):
    movie = get_object_or_404(Movie.objects.select_related('director'), pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

