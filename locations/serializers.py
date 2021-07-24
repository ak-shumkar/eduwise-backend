from . import models
from abstract.serializers import AbstractModelSerializer


class CountryI18NSerializer(AbstractModelSerializer):

    class Meta(AbstractModelSerializer.Meta):
        model = models.CountryI18N


class CountrySerializer(AbstractModelSerializer):
    translations = CountryI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Country
        depth = 1


class ProvinceI18NSerializer(AbstractModelSerializer):

    class Meta(AbstractModelSerializer.Meta):
        model = models.ProvinceI18N


class ProvinceSerializer(AbstractModelSerializer):
    translations = ProvinceI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Province


class CityI18NSerializer(AbstractModelSerializer):

    class Meta(AbstractModelSerializer.Meta):
        model = models.CityI18N


class CitySerializer(AbstractModelSerializer):
    translations = CityI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.City
