from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieSerializer, SerialSerializer, MusicSerializer

from .models import Movie, Serial, Music

@api_view()
def movie_list(request):
    movies_queryset = Movie.objects.all().select_related('director').prefetch_related('genre', 'cast')
    serializer = MovieSerializer(movies_queryset, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def movie_detail(request, pk):
    if request.method=='GET':
        movie = get_object_or_404(Movie.objects.select_related('director'), pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view()
def serial_list(request):
    series_queryset = Serial.objects.all().select_related('director').prefetch_related('genre', 'cast')
    serializer = SerialSerializer(series_queryset, many=True)
    return Response(serializer.data)

@api_view()
def serial_detail(request, pk):
    serial = get_object_or_404(Serial.objects.select_related('director'), pk=pk)
    serializer = SerialSerializer(serial)
    return Response(serializer.data)

@api_view()
def music_list(request):
    music_queryset = Music.objects.all().select_related('main_singer').prefetch_related('genre', 'other_singers')
    serializer = MusicSerializer(music_queryset, many=True)
    return Response(serializer.data)

@api_view()
def music_detail(request, pk):
    msuic = get_object_or_404(Music.objects.select_related('main_singer'), pk=pk)
    serializer = MusicSerializer(msuic)
    return Response(serializer.data)
