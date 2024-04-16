from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def movie_list(request):
    return Response('hello')

@api_view()
def movie_detail(request, pk):
    return Response(f'hello {pk}')

