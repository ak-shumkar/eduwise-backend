from django_filters import rest_framework as filters
from .models import Institution


class InstitutionFilter(filters.FilterSet):

    class Meta:
        model = Institution
        fields = ['city', 'institution_type']