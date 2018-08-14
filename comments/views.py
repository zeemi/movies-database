
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

