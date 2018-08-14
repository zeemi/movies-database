from django.db import transaction
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from libs.omdbapi import OpenMovieDatabase
from movies.utils import convert_dict_keys
from .serializers import MovieSerializer, MovieAddSerializer, RatingSerializer
from .models import Movie


class MovieViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)

    @transaction.atomic()
    def create(self, request, **kwargs):
        serializer = MovieAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie_definition = convert_dict_keys(OpenMovieDatabase().get_by_title(serializer.validated_data['title']))

        if self.queryset.filter(title=movie_definition['title']).exists():
            return Response(self.serializer_class(self.queryset.get(title=movie_definition['title'])).data)

        movie_serializer = self.get_serializer(data=movie_definition)
        movie_serializer.is_valid(raise_exception=True)
        self.perform_create(movie_serializer)

        ratings_serializer = RatingSerializer(data=[convert_dict_keys(rating) for rating in movie_definition['ratings']], many=True)
        if ratings_serializer.is_valid(raise_exception=True):
            ratings_serializer.save(movie=movie_serializer.instance)
        headers = self.get_success_headers(movie_serializer.data)
        return Response(movie_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

