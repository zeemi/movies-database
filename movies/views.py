from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from libs.omdbapi import OpenMovieDatabase
from movies.utils import convert_dict_keys
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

        serializer = self.get_serializer(data=convert_dict_keys(movie_definition))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

