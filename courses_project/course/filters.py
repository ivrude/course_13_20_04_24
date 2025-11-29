import django_filters
from django.db.models import Q


class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(method='by_title_filter')

    def by_title_filter(self, queryset, title, value):
        if value:
            value = value.strip()
            return queryset.filter(Q(title__icontains=value) | Q(description__icontains=value))
        else:
            return queryset.none()