from rest_framework import serializers

from .models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()

    def get_ratings(self, obj):
        return RatingSerializer(obj.rating_set.all(), many=True).data

    class Meta:
        model = Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    movie = None

    class Meta:
        model = Rating
        exclude = ('movie', 'id')


class MovieAddSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)