from . import models
from abstract.serializers import AbstractModelSerializer


class DegreeI18NSerializer(AbstractModelSerializer):

    class Meta(AbstractModelSerializer.Meta):
        model = models.DegreeI18N


class DegreeSerializer(AbstractModelSerializer):
    translations = DegreeI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Degree


class ProgramTypeDetailSerializer(AbstractModelSerializer):
    translations = DegreeI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Degree
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
        model = models.DegreeI18N


class FeeSerializer(AbstractModelSerializer):
    class Meta(AbstractModelSerializer.Meta):
        model = models.Fee


class ProgramSerializer(AbstractModelSerializer):
    translations = ProgramI18NSerializer(many=True, read_only=True)
    fee = FeeSerializer()

    class Meta(AbstractModelSerializer.Meta):
        model = models.Program
        depth = 1


class ApplicationSerializer(AbstractModelSerializer):
    class Meta(AbstractModelSerializer.Meta):
        model = models.Application
        fields = ['program', 'user']


class ApplicationDetailSerializer(AbstractModelSerializer):
    class Meta(AbstractModelSerializer.Meta):
        model = models.Application


class FacultyI18NSerializer(AbstractModelSerializer):
    class Meta(AbstractModelSerializer.Meta):
        model = models.FacultyI18N


class FacultySerializer(AbstractModelSerializer):
    translations = FacultyI18NSerializer(many=True, read_only=True)

    class Meta(AbstractModelSerializer.Meta):
        model = models.Faculty
