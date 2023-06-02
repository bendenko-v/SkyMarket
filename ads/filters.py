import django_filters

from ads.models import Ad


class AdFilterSet(django_filters.FilterSet):
    title = django_filters.filterset.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ('title',)
