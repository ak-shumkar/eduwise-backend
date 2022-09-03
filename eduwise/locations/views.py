from eduwise.abstract.paginations import StandardResultsSetPagination
from eduwise.abstract.views import AbstractViewSet
from eduwise.utils.permissions import ReadOnlyOrAdmin

from . import models, serializers


class CountryViewSet(AbstractViewSet):
    """ Country CREATE, UPDATE, GET and SET_INACTIVE (not DELETE) """
    model = models.Country
    serializer_class = serializers.CountrySerializer
    queryset = models.Country.objects.all()
    permission_classes = [ReadOnlyOrAdmin]


class CountryI18NViewSet(AbstractViewSet):
    """ CREATE, UPDATE, GET and DELETE country translations """
    model = models.Country
    serializer_class = serializers.CountryI18NSerializer
    queryset = models.CountryI18N.objects.all()
    permission_classes = [ReadOnlyOrAdmin]


class ProvinceViewSet(AbstractViewSet):
    """ Province CREATE, UPDATE, GET and SET_INACTIVE (not DELETE) """
    model = models.Province
    post_serializer_class = serializers.ProvinceSerializer
    list_serializer_class = serializers.ProvinceDetailSerializer
    queryset = models.Province.objects.all()
    permission_classes = [ReadOnlyOrAdmin]
    pagination_class = StandardResultsSetPagination


class ProvinceI18NViewSet(AbstractViewSet):
    """ CREATE, UPDATE, GET and DELETE province translations """
    model = models.ProvinceI18N
    serializer_class = serializers.ProvinceI18NSerializer
    queryset = models.ProvinceI18N.objects.all()
    permission_classes = [ReadOnlyOrAdmin]


class CityViewSet(AbstractViewSet):
    """ City CREATE, UPDATE, GET and SET_INACTIVE (not DELETE) """
    model = models.City
    post_serializer_class = serializers.CitySerializer
    list_serializer_class = serializers.CityDetailSerializer
    queryset = models.City.objects.all()
    permission_classes = [ReadOnlyOrAdmin]
    pagination_class = StandardResultsSetPagination


class CityI18NViewSet(AbstractViewSet):
    """ CREATE, UPDATE, GET and DELETE city translations """
    model = models.CityI18N
    serializer_class = serializers.CityI18NSerializer
    queryset = models.CityI18N.objects.all()
    permission_classes = [ReadOnlyOrAdmin]
