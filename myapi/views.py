from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import MovieSerializer, SerialSerializer, MusicSerializer, StaffSerializer
from .filters import MovieFilter, SerialFilter, MusicFilter
from .paginations import MoviePagination, SerialPagination, MusicPagination
from .models import Movie, Serial, Music, Staff
from .permissions import IsAdminOrReadOnly


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().select_related('director').prefetch_related('genre', 'cast')
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['year', 'rating', 'release_date']
    search_fields = ['title', 'director__first_name', 'director__last_name', 'director__nick_name', 'cast__first_name', 'cast__last_name', 'cast__nick_name']
    pagination_class = MoviePagination
    # filterset_fields = ['year', 'status', 'director', 'country', 'genre', 'cast']
    filterset_class = MovieFilter
    # permission_classes = [IsAdminOrReadOnly] # after finishing tokens, uncomment this to complete it.



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
    

class SerialViewSet(ModelViewSet):
    serializer_class = SerialSerializer
    queryset = Serial.objects.all().select_related('director').prefetch_related('genre', 'cast')
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['begin_year', 'end_year', 'rating']
    search_fields = ['title', 'director__first_name', 'director__last_name', 'director__nick_name', 'cast__first_name', 'cast__last_name', 'cast__nick_name']
    pagination_class = SerialPagination
    filterset_class = SerialFilter


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


class MusicViewSet(ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all().select_related('main_singer').prefetch_related('genre', 'other_singers')
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['year']
    search_fields = ['title', 'lyrics', 'main_singer__first_name', 'main_singer__last_name', 'main_singer__nick_name', 'other_singers__first_name', 'other_singers__last_name', 'other_singers__nick_name']
    pagination_class = MusicPagination
    filterset_class = MusicFilter


class StaffViewSet(ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated]) # don't forget to import action from rest_framework.decorators
    def me(self, request):
        # the url is http://127.0.0.1:8000/staff/me/
        user_id = request.user.id
        print(user_id)
        staff = Staff.objects.get(user_id=user_id)
        print(request.GET)
        print('tamam')
        if request.method=='GET':
            serializer = StaffSerializer(staff)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer = StaffSerializer(staff, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
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
