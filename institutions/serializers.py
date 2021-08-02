from rest_framework import serializers

from abstract.serializers import AbstractModelSerializer
from . import models


class InstitutionI18NSerializer(AbstractModelSerializer):
    class Meta(AbstractModelSerializer.Meta):
        model = models.InstitutionI18N
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['locale', 'institution'],
                message="This translation has already exists"
            )
        ]


class InstitutionSerializer(AbstractModelSerializer):
    translations = InstitutionI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Institution
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'city'),
                message="Institution with given name in given city has already exists"
            )
        ]


class InstitutionDetailSerializer(AbstractModelSerializer):
    translations = InstitutionI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Institution
        depth = 3


class PhotoSerializer(AbstractModelSerializer):
    class Meta(AbstractModelSerializer.Meta):
        model = models.Photo