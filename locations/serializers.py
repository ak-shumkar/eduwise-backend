from django.db.models import Q
from rest_framework import serializers

from . import models
from abstract.serializers import AbstractModelSerializer
from institutions.models import Institution


class CountryI18NSerializer(AbstractModelSerializer):

    class Meta(AbstractModelSerializer.Meta):
        model = models.CountryI18N


class CountrySerializer(AbstractModelSerializer):
    translations = serializers.SerializerMethodField()
    institutions_count = serializers.SerializerMethodField(read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Country
        depth = 1

    @staticmethod
    def get_institutions_count(country):
        return Institution.objects.filter(Q(city__country=country) | Q(city__province__country=country)).count()

    @staticmethod
    def validate_iso_code(value):
        if models.Country.objects.filter(iso_code=value.upper()).exists():
            raise serializers.ValidationError("Country with this iso code already exists")
        return value.upper()

    @staticmethod
    def get_translations(obj):
        result = dict()
        for translation in obj.translations.all():
            serializer = CountryI18NSerializer(translation)

            result.update({translation.locale: serializer.data})
        return result


class ProvinceI18NSerializer(AbstractModelSerializer):

    class Meta(AbstractModelSerializer.Meta):
        model = models.ProvinceI18N


class ProvinceSerializer(AbstractModelSerializer):
    translations = ProvinceI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Province


class ProvinceDetailSerializer(AbstractModelSerializer):
    translations = serializers.SerializerMethodField()
    country = CountrySerializer()

    class Meta(AbstractModelSerializer.Meta):
        model = models.Province
        depth = 2

    @staticmethod
    def get_translations(obj):
        result = dict()
        for translation in obj.translations.all():
            serializer = CountryI18NSerializer(translation)

            result.update({translation.locale: serializer.data})
        return result


class CityI18NSerializer(AbstractModelSerializer):

    class Meta(AbstractModelSerializer.Meta):
        model = models.CityI18N


class CitySerializer(AbstractModelSerializer):
    translations = CityI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.City


class CityDetailSerializer(AbstractModelSerializer):
    translations = serializers.SerializerMethodField()

    class Meta(AbstractModelSerializer.Meta):
        model = models.City
        depth = 1

    @staticmethod
    def get_translations(obj):
        result = dict()
        for translation in obj.translations.all():
            serializer = CountryI18NSerializer(translation)

            result.update({translation.locale: serializer.data})
        return result