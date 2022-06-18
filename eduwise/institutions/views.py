from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from eduwise.abstract.views import AbstractViewSet
from eduwise.utils.permissions import IsAdministrator, ReadOnlyOrAdmin
from . import models, serializers
from .filters import InstitutionFilter


class InstitutionTypeViewSet(AbstractViewSet):
    """ CREATE, GET, UPDATE, DELETE institution types"""
    model = models.InstitutionType
    queryset = models.InstitutionType.objects.all()
    serializer_class = serializers.InstitutionTypeSerializer
    permission_classes = [IsAdministrator]


class InstitutionViewSet(AbstractViewSet):
    """ CREATE, GET, UPDATE, DELETE universities """
    model = models.Institution
    queryset = models.Institution.objects.all()
    post_serializer_class = serializers.InstitutionSerializer
    list_serializer_class = serializers.InstitutionDetailSerializer
    permission_classes = [ReadOnlyOrAdmin]
    filter_backends = (SearchFilter, filters.DjangoFilterBackend)
    search_fields = ['name']
    filterset_class = InstitutionFilter


class InstitutionI18NViewSet(AbstractViewSet):
    """ CREATE, GET, UPDATE, DELETE universities translations """
    model = models.InstitutionI18N
    queryset = models.InstitutionI18N.objects.all()
    serializer_class = serializers.InstitutionI18NSerializer
    permission_classes = [IsAdministrator]


class PhotoViewSet(AbstractViewSet):
    """ CREATE, GET, UPDATE, DELETE universities gallery """
    model = models.Photo
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    permission_classes = [IsAdministrator]
