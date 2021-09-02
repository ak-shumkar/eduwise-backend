from . import models
from abstract.serializers import AbstractModelSerializer


class ProgramTypeI18NSerializer(AbstractModelSerializer):

    class Meta(AbstractModelSerializer.Meta):
        model = models.ProgramTypeI18N


class ProgramTypeSerializer(AbstractModelSerializer):
    translations = ProgramTypeI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.ProgramType


class ProgramTypeDetailSerializer(AbstractModelSerializer):
    translations = ProgramTypeI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.ProgramType
        depth = 1


class TermI18NSerializer(AbstractModelSerializer):
    class Meta(AbstractModelSerializer.Meta):
        model = models.TermI18N


class TermSerializer(AbstractModelSerializer):
    translations = TermI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Term


class TermDetailSerializer(AbstractModelSerializer):
    translations = TermI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Term
        depth = 1


class ProgramI18NSerializer(AbstractModelSerializer):
    class Meta(AbstractModelSerializer.Meta):
        model = models.ProgramTypeI18N


class ProgramSerializer(AbstractModelSerializer):
    translations = ProgramI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Program
