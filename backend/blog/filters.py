from django_filters.rest_framework import FilterSet, BaseInFilter, CharFilter

from .models import Blog


class CharFieldInFilter(BaseInFilter, CharFilter):
    pass


class BlogFilter(FilterSet):
    tags = CharFieldInFilter(method='filter_tags')

    def filter_tags(self, queryset, name, values):
        try:
            return queryset.filter(tags__id__in=values)
        except:
            return queryset.none()

    class Meta:
        model = Blog
        fields = ('tags',)
