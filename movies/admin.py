from django.contrib import admin

# Register your models here.
from .models import Movie, Rating


class FullReadOnlyMixin(object):
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]


class RatingInlineAdmin(admin.StackedInline, FullReadOnlyMixin):
    model = Rating
    exclude = ('id', )
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin, FullReadOnlyMixin):
    list_display = ('title', 'genre', 'imdb_rating')
    inlines = (RatingInlineAdmin, )

