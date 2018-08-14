from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from libs.omdbapi import OpenMovieDatabase
from .serializers import MovieSerializer, MovieAddSerializer
from .models import Movie


class MovieViewSet(mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    # def list(self, request):
    #     queryset = Movie.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)

    def create(self, request, **kwargs):
        serializer = MovieAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie_definition = OpenMovieDatabase().get_by_title(serializer.validated_data['title'])
        print(movie_definition)
        return super(MovieViewSet, self).create(request, **kwargs)