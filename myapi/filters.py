from django_filters.rest_framework import FilterSet

from .models import Movie, Serial, Music


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            "title": ["icontains"],
            "year": ["range", "exact", "lte", "gte"],
            "status": ["exact"],
            "director": ["exact"],
            # "director__first_name": ["icontains"],
            # "director__last_name": ["icontains"],
            # "director__nick_name": ["icontains"],
            "country": ["icontains"],
            "plot": ["icontains"],
            "rating": ["range"],
            "genre": ["exact"],
            "genre__title": ["icontains"],
            "cast": ["exact"],
            # "cast__first_name": ["icontains"],
            # "cast__last_name": ["icontains"],
            # "cast__nick_name": ["icontains"],
        }


class SerialFilter(FilterSet):
    class Meta:
        model = Serial
        fields = {
            "title": ["icontains"],
            "begin_year": ["range"],
            "end_year": ["range"],
            "director": ["exact"],
            # "director__first_name": ["icontains"],
            # "director__last_name": ["icontains"],
            # "director__nick_name": ["icontains"],
            "country": ["icontains"],
            "plot": ["icontains"],
            "rating": ["range"],
            "genre": ["exact"],
            "genre__title": ["icontains"],
            "cast": ["exact"],
            # "cast__first_name": ["icontains"],
            # "cast__last_name": ["icontains"],
            # "cast__nick_name": ["icontains"],
        }


class MusicFilter(FilterSet):
    class Meta:
        model = Music
        fields = {
            "title": ["icontains"],
            "year": ["range", "exact", "lte", "gte"],
            "main_singer": ["exact"],
            "genre": ["exact"],
            "genre__title": ["icontains"],
            "other_singers": ["exact"],
        }
