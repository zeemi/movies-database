
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        filter_kwargs = {}

        if 'movie' in self.request.GET:
            filter_kwargs['movie'] = self.request.GET['movie']

        return Comment.objects.filter(**filter_kwargs)

