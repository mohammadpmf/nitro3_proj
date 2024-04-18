from rest_framework.pagination import PageNumberPagination


class MoviePagination(PageNumberPagination):
    page_size=10


class SerialPagination(PageNumberPagination):
    page_size=10


class MusicPagination(PageNumberPagination):
    page_size=20