from abstract.serializers import AbstractModelSerializer
from . import models


class InstitutionI18NSerializer(AbstractModelSerializer):
    class Meta:
        model = models.InstitutionI18N


class InstitutionSerializer(AbstractModelSerializer):
    translations = InstitutionI18NSerializer(many=True, read_only=True)

    class Meta:
        model = models.Institution


class PhotoSerializer(AbstractModelSerializer):
    class Meta:
        model = models.Photo
