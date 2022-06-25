from django.db.models import F
from django_filters import rest_framework as filters
from .models import Institution


class InstitutionFilter(filters.FilterSet):
    price_min = filters.NumberFilter(method='min_price')
    price_max = filters.NumberFilter(method='max_price')

    class Meta:
        model = Institution
        fields = ['city', 'institution_type']

    @staticmethod
    def min_price(queryset, name, value):
        return queryset.annotate(total=F('fee__housing') + F('fee__tuition') + F('fee__other')).filter(total__gte=value)

    @staticmethod
    def max_price(queryset, name, value):
        return queryset.annotate(total=F('fee__housing') + F('fee__tuition') + F('fee__other')).filter(total__lte=value)
