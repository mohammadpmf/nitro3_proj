from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import MovieSerializer, SerialSerializer, MusicSerializer

from .models import Movie, Serial, Music


class MovieList(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().select_related('director').prefetch_related('genre', 'cast')


# class MovieList(APIView):
#     def get(self, request):
#         movies_queryset = Movie.objects.all().select_related('director').prefetch_related('genre', 'cast')
#         serializer = MovieSerializer(movies_queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         MovieSerializer.Meta.depth=0
#         serializer = MovieSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         MovieSerializer.Meta.depth=1
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method=='GET':
        movies_queryset = Movie.objects.all().select_related('director').prefetch_related('genre', 'cast')
        serializer = MovieSerializer(movies_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        MovieSerializer.Meta.depth=0
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        MovieSerializer.Meta.depth=1
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().select_related('director')


# class MovieDetail(APIView):
#     def get(self, request, pk):
#         movie = get_object_or_404(Movie.objects.select_related('director'), pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def put(self, request, pk):
#         movie = get_object_or_404(Movie.objects.select_related('director'), pk=pk)
#         MovieSerializer.Meta.depth=0
#         serializer = MovieSerializer(movie, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         MovieSerializer.Meta.depth=1
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def delete(self, request, pk):
#         movie = get_object_or_404(Movie.objects.select_related('director'), pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie.objects.select_related('director'), pk=pk)
    if request.method=='GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='PUT':
        MovieSerializer.Meta.depth=0
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        MovieSerializer.Meta.depth=1
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class SerialList(ListCreateAPIView):
    serializer_class = SerialSerializer
    queryset = Serial.objects.all().select_related('director').prefetch_related('genre', 'cast')


@api_view()
def serial_list(request):
    series_queryset = Serial.objects.all().select_related('director').prefetch_related('genre', 'cast')
    serializer = SerialSerializer(series_queryset, many=True)
    return Response(serializer.data)


class SerialDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SerialSerializer
    queryset = Serial.objects.select_related('director')


@api_view()
def serial_detail(request, pk):
    serial = get_object_or_404(Serial.objects.select_related('director'), pk=pk)
    serializer = SerialSerializer(serial)
    return Response(serializer.data)


class MusicList(ListCreateAPIView):
    serializer_class = MusicSerializer
    queryset = Music.objects.all().select_related('main_singer').prefetch_related('genre', 'other_singers')


@api_view()
def music_list(request):
    music_queryset = Music.objects.all().select_related('main_singer').prefetch_related('genre', 'other_singers')
    serializer = MusicSerializer(music_queryset, many=True)
    return Response(serializer.data)


class MusicDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = MusicSerializer
    queryset = Music.objects.all().select_related('main_singer').prefetch_related('genre', 'other_singers')


@api_view()
def music_detail(request, pk):
    msuic = get_object_or_404(Music.objects.select_related('main_singer'), pk=pk)
    serializer = MusicSerializer(msuic)
    return Response(serializer.data)
