from abstract.views import AbstractViewSet
from . import models, serializers
from utils.permissions import IsAdministrator


class CountryViewSet(AbstractViewSet):
    """ Country CREATE, UPDATE, GET AND SET_INACTIVE (not DELETE) """
    model = models.Country
    serializer_class = serializers.CountrySerializer
    queryset = models.Country.objects.all()
    permission_classes = [IsAdministrator]


class CountryI18NViewSet(AbstractViewSet):
    """ CREATE, UPDATE, GET AND DELETE country translations """
    model = models.Country
    serializer_class = serializers.CountryI18NSerializer
    queryset = models.CountryI18N.objects.all()
    permission_classes = [IsAdministrator]


class ProvinceViewSet(AbstractViewSet):
    """ Province CREATE, UPDATE, GET AND SET_INACTIVE (not DELETE) """
    model = models.Province
    post_serializer_class = serializers.ProvinceSerializer
    list_serializer_class = serializers.ProvinceDetailSerializer
    queryset = models.Province.objects.all()
    permission_classes = [IsAdministrator]


class ProvinceI18NViewSet(AbstractViewSet):
    """ CREATE, UPDATE, GET AND DELETE province translations """
    model = models.ProvinceI18N
    serializer_class = serializers.ProvinceI18NSerializer
    queryset = models.ProvinceI18N.objects.all()
    permission_classes = [IsAdministrator]


class CityViewSet(AbstractViewSet):
    """ City CREATE, UPDATE, GET AND SET_INACTIVE (not DELETE) """
    model = models.City
    post_serializer_class = serializers.CitySerializer
    list_serializer_class = serializers.CityDetailSerializer
    queryset = models.City.objects.all()
    permission_classes = [IsAdministrator]


class CityI18NViewSet(AbstractViewSet):
    """ CREATE, UPDATE, GET AND DELETE city translations """
    model = models.CityI18N
    serializer_class = serializers.CityI18NSerializer
    queryset = models.CityI18N.objects.all()
    permission_classes = [IsAdministrator]
