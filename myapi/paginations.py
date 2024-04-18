from rest_framework.pagination import PageNumberPagination

class MoviePagination(PageNumberPagination):
    page_size=10