from django.db.models import F
from django_filters import rest_framework as filters
from .models import Institution


class InstitutionFilter(filters.FilterSet):
    price_min = filters.NumberFilter(method='min_price')
    price_max = filters.NumberFilter(method='max_price')
    program = filters.CharFilter(method='by_program')
    category = filters.NumberFilter(method='by_category')

    class Meta:
        model = Institution
        fields = ['city', 'institution_type']

    @staticmethod
    def by_program(queryset, name, program_name):
        """Search institutions by program"""
        return queryset.filter(programs__title__contains=program_name)

    @staticmethod
    def by_category(queryset, name, category):
        """Search institutions by faculty"""
        return queryset.filter(programs__faculty_id=category)

    @staticmethod
    def min_price(queryset, name, value):
        """Search institutions with minimum given total fee"""
        return queryset.annotate(total=F('fee__housing') + F('fee__tuition') + F('fee__other')).filter(total__gte=value)

    @staticmethod
    def max_price(queryset, name, value):
        """Search institutions with maximum given total fee"""
        return queryset.annotate(total=F('fee__housing') + F('fee__tuition') + F('fee__other')).filter(total__lte=value)
