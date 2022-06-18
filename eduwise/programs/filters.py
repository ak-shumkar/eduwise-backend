from django_filters import rest_framework as filters

from .models import Program


class ProgramFilters(filters.FilterSet):
    class Meta:
        model = Program
        fields = ['institution', 'degree']